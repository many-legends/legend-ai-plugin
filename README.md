# Legend AI plugins

Connect Claude or ChatGPT to your Legend account. Read balances, positions, orders, and fills. Prepare an exact perpetual limit-order proposal, then review it in Legend. The default connection cannot execute orders, transfer funds, or withdraw funds.

## Connect Claude

1. Open [Claude connector settings](https://claude.ai/customize/connectors).
2. Select **Add custom connector**, name it **Legend**, and enter `https://app.legend.trade/api/connectors/mcp`.
3. Connect, sign in to Legend, and approve access to your own account.
4. Ask: **Show my Legend username, network, and available-to-trade estimate.**

Team and Enterprise users may need an administrator to add the connector. Each user must connect their own Legend account. All returned balances refer to mainnet. There is no paper mode.

## Add workflows

| Package | Where to use it | Connection |
| --- | --- | --- |
| [Legend](plugins/legend) | Claude web or desktop plugin interface | Bundles the hosted MCP connector; complete OAuth in Claude |
| [Legend workflows](plugins/legend-code) | Claude Code | Uses the connector you connected on claude.ai |
| [Legend for OpenAI](plugins/legend-openai) | ChatGPT and Codex submission | OAuth package prepared; developer verification and review are pending |

In Claude, open **Customize > Plugins > Add > Add marketplace** and enter `many-legends/legend-ai-plugin`. Install **Legend**, open its **Connectors** tab, and connect your account. You can also upload a release ZIP.

In Claude Code 2.1.275 or later, first connect Legend on claude.ai, then sign in to Claude Code with the same claude.ai subscription account. Install the workflows:

```text
/plugin install legend-code --marketplace many-legends/legend-ai-plugin
```

Run `/mcp` and check for **claude.ai Legend**. The Code package contains skills only. It does not add a local server that would override the hosted connection. Direct localhost OAuth and API-key-only Claude Code sessions are not supported by this package. See [Anthropic's hosted connector instructions](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai).

## Try these requests

- Show my Legend account, open positions, and open orders.
- Show my latest three fills and their fees.
- Prepare a BTC perpetual buy limit proposal for 0.001 BTC at $60,000, GTC, with reduce-only off. Do not place the order.

Choose the exact order terms yourself. A proposal changes no position and reserves no funds. Open its review link, check current account and market conditions, and submit through Legend if you choose to proceed. Proposal links expire after 15 minutes.

## Availability and distribution

The production connector rollout was opened to all Legend users on November 13, 2026. Account authentication, consent, permissions, expiry, and revocation still apply. The source removal of the old access flag and public documentation are tracked in [frontend PR 10568](https://github.com/many-legends/legend-frontend/pull/10568).

The Legend MCP directory submission in Claude is **in review**. No approved Claude plugin listing or OpenAI directory publication is claimed. You can use the custom connection and public source without a directory listing. Fresh end-to-end tests of each host remain separate from package validation.

Read the [Legend connection guide](https://docs.legend.trade/api-reference/connectors/overview). Privacy: [legend.trade/privacy](https://legend.trade/privacy). Terms: [legend.trade/terms](https://legend.trade/terms). Support: support@legend.trade. Never paste a key, password, token, or wallet secret into chat. Revoke the associated API key in Legend **Settings > Trading** to stop future credential use. Revocation does not close positions or cancel orders.

## Build and validate

```sh
python3 scripts/package.py --out /absolute/path/outside-this-repo
claude plugin validate . --strict
claude plugin validate ./plugins/legend --profile directory --strict
claude plugin validate ./plugins/legend-code --profile directory --strict
```

The build checks package paths, workflow consistency, public metadata, and the exact MCP endpoint. It creates ZIPs and a SHA-256 checksum file. OpenAI portal validation, hosted authentication, and directory review are separate checks. The Claude package is the source for shared workflows; keep the copies in the Code and OpenAI packages equal.

## License

MIT. See [LICENSE](LICENSE). The license does not grant rights to use Legend trademarks.
