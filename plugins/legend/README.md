# Legend for Claude

Install this plugin in Claude web or desktop to check your Legend account, review positions and fills, and prepare exact perpetual limit-order proposals. Connect through the plugin Connectors tab using OAuth. Each user signs in to their own account.

The server is https://app.legend.trade/api/connectors/mcp. It cannot execute orders or transfer or withdraw funds. All accounts use mainnet. Proposal links expire after 15 minutes. Review the order in Legend before submitting it.

For setup, current distribution status, example prompts, permissions, privacy, and support, see the [repository guide](../../README.md) and [Legend docs](https://docs.legend.trade/api-reference/connectors/overview).

For Claude Code, use the separate legend-code package with your claude.ai connection. This hosted plugin can add a local MCP entry in Code, which would take precedence over the hosted connection. Localhost OAuth is not supported.

The source uses the MIT license. Directory approval is separate from this public package. Contact support@legend.trade. Privacy: https://legend.trade/privacy. Terms: https://legend.trade/terms.
