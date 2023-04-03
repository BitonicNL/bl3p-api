# Authenticated API | HTTP Calls

## Table of contents

1. Introduction
2. Basic functions
   1. Create an order
   2. Cancel an order
   3. Get a specific order
   4. Get the whole orderbook

3. Account info & functions
   1. Get the transaction history
   2. Create a new deposit address
   3. Get the last deposit address
   4. Create a withdrawal
   5. Get account info & balance
   6. Get active orders
   7. Get order history
   8. Fetch all trades on BL3P

4. Appendix
   1. Error code
   2. Rate limiting

---

## 1 - Introduction

This document describes the usage of the private HTTP API of BL3P.
In the file one directory above you can find the base.md file.
The base.md document describes all basic details that you need to know to use the BL3P API.
If you would like to know how to make a connection to the BL3P API, please check the examples that are available one directory above.

## 2 - Basic functions

**Definition of the path variable order:**
```text
/<version>/<market>/<namespace>/<callname>[/<subcallname>]
```
___
**Description of the path variables:**

Version of API (is currently: 1)
```text
<version> = 1
```
___
Market that the call will be applied to.

Note: GENMKT is used for market independent calls
```text
<market> = BTCEUR, LTCEUR, GENMKT
```
___
Namespace of call. Usually: "money"
```text
<namespace> = $namespace
```
___
Name of call (for example: “order”)
```text
<callname> = $callname
```
___
Name of subcall, (for example: “add”)
```text
<subcallname> = $subcallname
```
___

The response is a success or an error. In case of result: success, the requested data will be returned.
In case of an error, an error code will be returned. The possible error codes are listed in the appendix.

## 2.1 - Create an order

### Call

```text
<market>/money/order/add
```

### Request
`type` string
```
'bid', 'ask'
```
___
`amount_int` int
```
Amount BTC, amount LTC (*1e8)
```
The field described above is optional. _When omitted, amount_funds_int is required. Also note that this field and the amount_funds_int field cannot both be set when the price field is also set. When the price field is not set this field can be set when amount_funds_int is also set._
___
`price_int` int
```
Limit price in EUR (*1e5)
```
The field described above is optional. _When omitted, order will be executed as a market order._
___
`amount_funds_int` int
```
Maximal EUR amount to spend (*1e5)
```
The field described above is optional. _When omitted, amount_int is required. Also note that this field and the amount_int field cannot both be set when the price field is also set. When the price field is not set this field can be set when amount_int is also set._
___
`fee_currency` string
```
Currency the fee is accounted in. Can be: 'EUR' or 'BTC'
```
>___

### Response
`order_id` int
```
The id of the order.
```

## 2.2 - Cancel an order

### Call

```text
<market>/money/order/cancel
```

### Request
`order_id` int
```
The id of the order that you wish to cancel.
```

### Response
```
For this call there is no specific result returned other then
the result of the call which contains: 'success' or 'failed' and an optional error array.
```


## 2.3 - Get a specific order
### Call
```text
<market>/money/order/result
```

### Request
`order_id` int
```
The id of the order that you wish to retrieve.
```

### Response
`order_id` int
```
Id of the order.
```
___
`label` string
```
API-key label
```
___
`currency` string
```
Currency of the order. (Is now by default 'EUR')
```
___
`item` string
```
The item that will be traded for `currency`. (Can be: 'BTC')
```
___
`type` string
```
Type of order. (Can be: 'bid', 'ask')
```
___
`amount` amountObj
```
Total order amount of BTC or LTC.
```
The field described above is optional
___
`price` amountObj
```
Order limit price.
```
The field described above is optional
___
`status` string
```
Status of the order. (Can be: ’pending’, ‘open’, ‘closed’, ‘cancelled’, ’placed’)
```
___
`date` timestamp
```
The time the order got added.
```
___
`date_closed` timestamp
```
The time the order got closed. (not available for marketorders and cancelled orders)
```
___
`total_amount` amountObj
```
Total amount of the trades that got executed. (Can be: BTC or LTC).
```
___
`total_spent` amountObj
```
Total amount in EUR of the trades that got executed.
```
___
`total_fee` amountObj
```
Total fee incurred in BTC or LTC.
```
___
`avg_cost` amountObj
```
Average cost of executed trades.
```
The field described above is optional
___
`trades` array
```
Array of trades executed for the regarding order.
```
**Each array item of 'trade' will contain:**
`amount` amountObj
```
BTC or LTC amount.
```
___
`currency` string
```
Currency of the regarding trade.
```
___
`date` timestamp
```
The time of the trade execution.
```
___
`item` string
```
'BTC'
```
___
`price` amountObj
```
Price of the executed trade in EUR.
```
___
`trade_id` int
```
Id of trade.
```

>___

## 2.4 - Get the whole orderbook

### Call

```text
<market>/money/depth/full
```

### Request

```
There are no specific parameters required for this call.
```

### Response
`asks` array
```
Array of asks that are in the orderbook.
```

`bids` array
```
Array of bids that are in the orderbook.
```

**Each array item of 'asks' will contain:**

`amount_int` int
```
Amount BTC, amount LTC (*1e8)
```
___
`price_int` int
```
Limit price in EUR (*1e5)
```
___
`count` int
```
Count of orders at this price.
```

**Each array item of 'bids' will contain:**

`amount_int` int
```
Amount BTC, amount LTC (*1e8)
```
___
`price_int` int
```
Limit price in EUR (*1e5)
```
___
`count` int
```
Count of orders at this price.
```

>___

## 3 - Account info & functions

## 3.1 - Get the transaction history

### Call

```text
GENMKT/money/wallet/history
```

### Request

`currency` string
```
Currency of the wallet. (Can be: 'BTC', 'EUR')
```
___
`page` int
```
Page number. (1 = most recent transactions)
```
The field described above is optional, default is 1
___
`date_from` timestamp
```
Filter the result by a Unix-timestamp. Transactions before this date will not be returned.
```
The field described above is optional, default is no filter
___
`date_to` timestamp
```
Filter the result by a Unix-timestamp. Transactions after this date will not be returned.
```
The field described above is optional, default is no filter
___
`type` string
```
Filter the result by type. (Can be: ‘trade’, ‘fee’, ‘deposit’, ‘withdraw’)
```
The field described above is optional, default is no filter
___
`recs_per_page` int
```
Number of records per page.
```
The field described above is optional, default is 10
>___

### Response

`page` int
```
Current page number.
```
___
`records` int
```
Count of records in the result set.
```
___
`max_page` int
```
Number of last page.
```
___
`transactions` array
```
Array of transactions.
```
**Each array item of 'transactions' will contain:**
`transaction_id` int
```
Id of the transaction.
```
`amount` amountObj
```
BTC or LTC amount.
```
___
`date` timestamp
```
Time when the regarding transaction took place.
```
___
`debit_credit` string
```
Type of booking. (Can be: 'debit' or 'credit')
```
___
`price` amountObj
```
Price of the executed trade.
```
The field described above is for type 'trade' only and will be omitted if recs_per_page > 1000
___
`order_id` int
```
Id of the order.
```
The field described above is for type 'trade' only and will be omitted if recs_per_page > 1000
___
`type` string
```
Type of transaction (Can be: 'trade’, ‘fee’, ‘deposit’, ‘withdraw’)
```
___
`balance` amountObj
```
Balance of the user his account (for the regarding currency) after the transaction.
```
___
`trade_id` int
```
Id of the trade.
```
The field described above is for type 'trade' only and will be omitted if recs_per_page > 1000
___
`contra_amount` amountObj
```
Contra amount of the trade.
```
The field described above is for type 'trade' only and will be omitted if recs_per_page > 1000
___
`fee` amountObj
```
Fee incurred by the regarding trade
```
The field described above is for type 'trade' only and will be omitted if recs_per_page > 1000


>___

## 3.2 - Create a new deposit address

### Call

```text
GENMKT/money/new_deposit_address
```

### Request

`currency` string
```
Currency (Can be: 'BTC')
```

### Response

`address` string
```
Deposit address for the requested currency
```

## 3.3 - Get the last deposit address

### Call

```text
GENMKT/money/deposit_address
```

### Request

`currency` string
```
currency (Can be: 'BTC')
```

### Response

`address` string
```
Deposit address for the requested currency
```

## 3.4 - Create a withdrawal

### Call

```text
GENMKT/money/withdraw
```

### Request

`currency` string
```
Currency (Can be: 'BTC','EUR')
```
___
`account_id` string
```
IBAN account-id (that is available within the regarding BL3P account)
```
`account_name` string
```
IBAN account-name (should match your account verification)
```

**or**

`address` string
```
The address to withdraw to
```
`extra_fee` int (use 1 for extra fee) (deprecated, please use fee_priority)
```
This will send the withdrawal as priority, extra fee will be charged (see bl3p.eu) (deprecated, please use fee_priority)
```
The field described above is optional, default is no extra fee
___
`fee_priority` string (low | medium | high)
```
This will send the withdrawal as low, medium or high priority
```
The field described above is optional, default is medium
___
`amount_int` int
```
Satoshis or 0,00001 EUR
```

### Response

`id` int
```
Id of the withdrawal
```

## 3.5 - Get account info & balance
### Call

```text
GENMKT/money/info
```

### Request

```
There are no specific parameters required for this call.
```

### Response

`user_id` int
```
Id of the user.
```
___
`trade_fee` float
```
Percentage fee for the user
```
___
`wallets` object
```
Object of wallets, the object will contain the following keys: BTC, LTC, EUR
```
**Each wallet item of 'wallets' will contain:**

`balance` amountObj
```
Balance in this wallet
```
___
`available` amountObj
```
Available in this wallet.
```

>___

## 3.6 Get active orders
### Call
```text
<market>/money/orders
```

### Request

```
There are no specific parameters required for this call.
```

### Response

`orders` array
```
Array of active orders.
```
**Each array item of 'orders' will contain:**

`order_id` int
```
Id of the order.
```
___
`label` string
```
API-key label
```
___
`currency` string
```
Currency of the order. (Is now by default 'EUR')
```
___
`item` string
```
The item that will be traded for `currency`. (Can be: 'BTC')
```
___
`type` string
```
Type of order. (Can be: 'bid', 'ask')
```
___
`status` string
```
Status of the order. (Can be: ‘open’, ’placed’)
```
___
`date` timestamp
```
The time the order got added.
```
___
`amount` amountObj
```
Total order amount of BTC or LTC.
```
The field described above is optional
___
`amount_funds_executed` amountObj
```
Amount in funds that is executed.
```
___
`amount_executed` amountObj
```
Amount that is executed.
```
___
`price` amountObj
```
Order limit price.
```
The field described above is optional
___
`amount_funds` amountObj
```
Maximal EUR amount to spend (*1e5)
```
The field described above is optional

>___

## 3.7 Get order history
### Call
```text
<market>/money/orders/history
```

### Request

`page` int
```
Page number. (1 = most recent transactions)
```
The field described above is optional, default is 1
___
`date_from` timestamp
```
Filter the result by a Unix-timestamp. Transactions before this date will not be returned.
```
The field described above is optional, default is no filter
___
`date_to` timestamp
```
Filter the result by a Unix-timestamp. Transactions after this date will not be returned.
```
The field described above is optional, default is no filter
___
`recs_per_page` int
```
Number of records per page.
```
The field described above is optional, default is 100

>___

### Response

`page` int
```
Current page number.
```
___

`records` int
```
Count of records in the result set.
```
___
`max_page` int
```
Number of last page.
```
`orders` array
```
Array of active orders.
```
**Each array item of 'orders' will contain:**

`order_id` int
```
Id of the order.
```
___

`label` string
```
API-key label
```
___
`currency` string
```
Currency of the order. (Is now by default 'EUR')
```
___
`item` string
```
The item that will be traded for `currency`. (Can be: 'BTC')
```
___
`type` string
```
Type of order. (Can be: 'bid', 'ask')
```
___
`status` string
```
Status of the order. (Can be: ‘closed’, ‘cancelled’)
```
___
`date` timestamp
```
The time the order got added.
```
___
`date_closed` timestamp
```
The time the order got closed.
```
___
`amount` amountObj
```
Total order amount of BTC or LTC.
```
The field described above is optional
___
`amount_funds_executed` amountObj
```
Amount in funds that is executed.
```
___
`amount_executed` amountObj
```
Amount that is executed.
```
___
`price` amountObj
```
Order limit price.
```
The field described above is optional
___
`amount_funds` amountObj
```
Maximal EUR amount to spend (*1e5)
```
The field described above is optional

>___

## 3.8 - Fetch all trades on BL3P

### Call

```text
<market>/money/trades/fetch
```

### Request

`trade_id` int
```
Id of the trade after which you want to fetch the (next) 1000 trades
```
The field described above is optional, if this field isn't specified, this call will return the last 1000 trades.

>___

### Response

`trades` array
```
Array of trades.
```
**Each array item of 'trades' will contain:**
`trade_id` int
```
Id of the trade.
```
___
`date` timestamp (in milliseconds)
```
The time of the trade execution.
```
___
`amount_int` int
```
Amount traded. (*1e8)
```
___
`price_int` int
```
Price of the traded item in EUR. (*1e5)
```

>___


## 4 - Appendix

## 4.2 - Error codes

The API can respond to invalid calls with the following error messages:

`AMOUNT_FUNDS_LESS_THAN_MINIMUM`
```
Order amount (amount_funds) smaller than the minimum.
```
___

`AMOUNT_LESS_THAN_MINIMUM`
```
Order amount is smaller than the minimum
```
___

`INSUFFICIENT_FUNDS`
```
Not enough money on account for this order.
```
___

`INVALID_AMOUNT`
```
Invalid field 'amount_int'.
```
___

`INVALID_AMOUNT_FUNDS`
```
Invalid field 'amount_funds_int'.
```
___

`INVALID_FEE_CURRENCY`
```
Invalid field 'fee_currency'.
```
___

`INVALID_LIMIT_ORDER`
```
Limitorders can't have both an 'amount' and an 'amount_funds'.
```
___

`INVALID_PRICE`
```
Invalid field 'price_int'.
```
___

`INVALID_TYPE`
```
Invalid field type (‘bid’ or ‘ask’).
```
___

`KEY_MISSING`
```
The Rest-Key header misses.
```
___

`LIMIT_REACHED`
```
User has done to much calls.
```
___

`MARKETPLACE_INACCESSIBLE`
```
Market (temporarily) closed.
```
___

`MARKETPLACE_NOT_ACCEPTING_ORDERS`
```
Market does (temporarily) not accepts orders.
```
___

`MISSING_AMOUNT`
```
The field 'amount' or 'amout_funds' is missing with this order.
```
___

`MISSING_FIELD`
```
A required field at this call is missing.
```
___

`NOT_AUTHENTICATED`
```
Signature-key-combination is invalid.
```
___

`SIGN_MISSING`
```
The Rest-Sign header misses.
```
___

`UNKNOWN_ACCOUNT`
```
User has no account for given currency (SystemServer)
```
___

`UNKNOWN_CURRENCY`
```
The requested currency doesn't exist.
```
___

`UNKNOWN_ERROR`
```
An unknown server error occured.
```
___

`UNKNOWN_MARKETPLACE`
```
The requested market doesn't exist.
```
___

`UNKNOWN_ORDER`
```
The order to cancel or fetch doesn't exist
```
___


`UNKNOWN_PATH`
```
Requested path and/or call doesn't exist.
```
___

## 4.2 - Rate limiting

| Call type                   | Count |
|-----------------------------|-------|
| <market>/money/depth/full   | 30    |
| GENMKT/money/wallet/history | 300   |
| <market>/money/trades/fetch | 100   |
| all other calls             | 600   |
   
The first column describes the call type and the second column represents the regarding amount of calls one can execute successfully per 5 minutes.
