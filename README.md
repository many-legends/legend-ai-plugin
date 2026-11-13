# Legend AI plugin

Official Legend plugin source for Claude. The plugin uses Legend's remote MCP server to read your account and prepare orders for review in Legend. It does not execute orders or move funds.

## Install

In Claude Code 2.1.275 or later:

```text
/plugin install legend --marketplace many-legends/legend-ai-plugin
```

In Claude, add this repository as a marketplace under Customize > Plugins > Add > Add marketplace, then install Legend. You can also upload the plugin ZIP. Open the plugin Connectors tab and connect your own Legend account through OAuth.

## Workflows

- Account check: balances, positions, and open orders.
- Trade-history review: fills, fees, and order status.
- Order preparation: an exact perpetual GTC limit-order proposal for review in Legend.

The plugin does not choose size or leverage for you. All account values refer to mainnet. It has no simulated account and no transfer or withdrawal tools. Never paste a key, token, password, or wallet secret into chat.

## Current availability

As checked on November 13, 2026, production MCP access remains restricted by the ai-connectors-enabled flag. The source is public, but ordinary Legend accounts cannot yet complete OAuth. This repository is not a published Claude directory listing. Fresh hosted OAuth and tool checks, the public access rollout, and directory review remain pending. Local package validation does not establish that those steps passed.

See [the plugin guide](plugins/legend/README.md) for setup, privacy, and support. The privacy policy is https://legend.trade/privacy. Contact support@legend.trade. Source code uses the MIT license. The license does not grant rights to use Legend trademarks.

## Validate

```sh
claude plugin validate . --strict
claude plugin validate ./plugins/legend --profile directory --strict
```
