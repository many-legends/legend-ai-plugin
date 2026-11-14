"""Validate Legend packages and create credential-free release ZIPs."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = 'https://app.legend.trade/api/connectors/mcp'
PACKAGES = {'legend': 'legend-claude', 'legend-code': 'legend-code', 'legend-openai': 'legend-openai'}


def validate(name):
    package = ROOT / 'plugins' / name
    manifest = package / ('plugin.json' if name == 'legend-openai' else '.claude-plugin/plugin.json')
    data = json.loads(manifest.read_text())
    assert data['name'] == ('legend' if name == 'legend-openai' else name)
    assert data['license'] == 'MIT'
    assert data['repository'] == 'https://github.com/many-legends/legend-ai-plugin'
    assert (package / 'LICENSE').read_text() == (ROOT / 'LICENSE').read_text()
    assert len((package / 'README.md').read_text().split()) >= 40
    canonical = ROOT / 'plugins/legend/skills'
    skills = list((package / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 3
    for skill in skills:
        assert skill.read_bytes() == (canonical / skill.parent.name / 'SKILL.md').read_bytes()
    if name == 'legend-code':
        assert not (package / '.mcp.json').exists()
    else:
        config = json.loads((package / ('mcp.json' if name == 'legend-openai' else '.mcp.json')).read_text())
        assert set(config['mcpServers']) == {'legend'}
        server = config['mcpServers']['legend']
        assert server['url'] == ENDPOINT and not server.get('headers')
        assert server['type'] == ('streamable-http' if name == 'legend-openai' else 'http')
        if name == 'legend-openai':
            assert server['extensions']['com.openai']['auth'] == {
                'type': 'oauth', 'client': {'mode': 'cimd'}, 'baseScopes': ['legend:read']}
            interface = data['extensions']['com.openai']['interface']
            for field in ['composerIcon', 'logo']:
                asset = (package / interface[field]).resolve()
                assert asset.is_relative_to(package.resolve()) and asset.is_file()
    for path in package.rglob('*'):
        assert not path.is_symlink()
        assert path.name not in {'.env', '.env.local', 'credentials.json'}
    return package, data['version']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    validated = [(name, *validate(name)) for name in PACKAGES]
    assert len({version for _, _, version in validated}) == 1
    marketplace = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    assert {item['name'] for item in marketplace['plugins']} == {'legend', 'legend-code'}
    print('Validated all three packages and shared workflows.')
    if not args.out:
        return
    output = args.out.resolve()
    assert not output.is_relative_to(ROOT), 'Keep release ZIPs outside the source repository.'
    output.mkdir(parents=True, exist_ok=True)
    checksums = []
    for name, package, version in validated:
        target = output / f'{PACKAGES[name]}-{version}.zip'
        assert not target.exists(), f'Release artifact already exists: {target}'
        with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob('*')):
                if path.is_file():
                    archive.write(path, path.relative_to(package))
        with zipfile.ZipFile(target) as archive:
            assert archive.testzip() is None
        checksums.append(f'{hashlib.sha256(target.read_bytes()).hexdigest()}  {target.name}')
        print(target.name)
    (output / 'SHA256SUMS').write_text('\n'.join(checksums) + '\n')


if __name__ == '__main__':
    main()
