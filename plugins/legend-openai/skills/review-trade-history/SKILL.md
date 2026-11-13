---
name: review-trade-history
description: Review your Legend fills, fees, or a specific order when the user asks about trade history or order status.
---

Use fresh Legend connector results for the requested account and period.

1. Use list_fills for executed trades and fees. Use list_orders for order history. Follow pagination until the requested range is complete or the requested count is reached. State any remaining limit.
2. Use get_order for a specific order reference supplied by the user or returned by an account read. Never invent an order reference.
3. Use get_operation only for a known operation ID when the user needs to reconcile an earlier request. An unknown outcome is not a failed trade. Do not retry an order or create a replacement intent.
4. Use display fields for human-readable prices and amounts. Keep fills, pending orders, canceled orders, and fees distinct. Do not calculate investment returns from an incomplete fill sample or assume that deposits are profit.
5. Answer with the requested records and any limits. If access has expired, direct the user to reconnect Legend. Never ask for credentials in chat.

This workflow reads records. It cannot place, change, or cancel an order. Do not send account records to another service unless the user requests that destination.
