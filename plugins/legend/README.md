# Legend for Claude

Legend connects Claude to your Legend account through a remote MCP server. The plugin adds three workflows: check balances and positions, review fills and order status, and prepare a perpetual limit-order proposal for review in Legend.

## Install and connect

Upload the plugin ZIP in Claude under Customize > Plugins > Add > Upload plugin. Open the plugin Connectors tab, connect Legend, and complete the Legend OAuth sign-in flow. On a team plan, an owner may need to add the connector first. Never paste credentials into chat.

The server URL is https://app.legend.trade/api/connectors/mcp. It reads account data and prepares proposals. It does not execute orders or transfer or withdraw funds. Each user connects their own account. All balances and proposals refer to mainnet. No simulated account is provided.

## Preview access

As checked on November 13, 2026, access remains limited by the ai-connectors-enabled production flag. Ordinary Legend users cannot yet connect. This package is not a published Claude directory listing. Local validation does not establish live OAuth or tool success.

## Example prompts

- Show my Legend account, open positions, and open orders.
- Show my latest three fills and their fees.
- Prepare a BTC buy limit proposal for 0.001 BTC at 60000, GTC, with reduce-only false. Do not place it.

## Privacy and support

Legend account requests go to the Legend service after OAuth consent. Read the privacy policy at https://legend.trade/privacy and terms at https://legend.trade/terms. Contact support@legend.trade for help. Revoke access through the associated Trading API key in Legend Settings > Trading. This package contains no credentials.

## Distribution status

The plugin source uses the MIT license. Anthropic directory submission and review remain pending. A public GitHub repository is not a public Claude directory listing.

## Claude Code install

After this repository is published, use Claude Code 2.1.275 or later:

```text
/plugin install legend --marketplace many-legends/legend-ai-plugin
```

Live Claude Code OAuth has not yet been verified. Use the Claude account connection checks before reporting it as working.
