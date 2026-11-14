# Legend workflows for Claude Code

This package contains account, trade-history, and order-review skills. It uses the Legend connector you authenticated on claude.ai. It does not add a local MCP server or contain credentials.

First add https://app.legend.trade/api/connectors/mcp as a custom connector on claude.ai and complete Legend OAuth. Sign in to Claude Code with the same claude.ai subscription account. Install legend-code from this marketplace, then use /mcp to check for claude.ai Legend. API-key-only Code sessions do not load claude.ai connectors.

If a local server for the same URL hides the hosted connector, inspect /mcp before changing that local entry. Do not paste credentials into chat. This package cannot execute orders or move funds. Use the [repository guide](../../README.md) for examples, privacy, support, and current verification limits. See [Anthropic's documentation](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai).

Install after connecting on claude.ai:

```text
/plugin install legend-code --marketplace many-legends/legend-ai-plugin
```
