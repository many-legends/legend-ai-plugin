---
name: prepare-order-review
description: Prepare a Legend perpetual limit-order proposal when the user asks to review a trade in Legend before submitting it.
---

Use the Legend connector prepare_order tool only when the user requests an order proposal.

1. Establish the market, buy or sell side, base-asset size, exact limit price, and reduce-only setting. Ask for missing values. Do not choose a size, leverage, price, or side for the user. Supported proposals are perpetual GTC limit orders.
2. Call prepare_order with the exact requested values. If validation fails, explain the error and ask for corrected values. Do not silently round, change, or replace the requested order.
3. Return the review_url provided by the tool and the returned market, side, size, price, and reduce-only value. Use the server display fields for prices and amounts.
4. State that no order was placed. The user must open Legend, check the account, size, price, and order terms, and submit through the normal trade form.

This connector cannot execute an order, transfer funds, or withdraw funds. Do not call the execution endpoint or claim that a proposal is an executed trade. The endpoint is mainnet only; do not claim that it provides simulated trading. If the user requests an unsupported order type, explain the limitation. Never ask for credentials or wallet secrets in chat.
