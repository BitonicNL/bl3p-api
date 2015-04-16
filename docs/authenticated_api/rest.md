# Authenticated API | REST Calls

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
  7. Get the last 1000 trades after an specific trade

4. Appendix - Error code

---

## 1 - Introduction

This document describes the usage of the private REST API of BL3P.
In the file on directory above you can find the base.md file.
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
Namespace of call. Usualy: "money"
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

The response is a succes or an error. In case of result: succes, the requested data will be returned.
In case of an error, an error code will be retuned. The possible error codes are listed in the appendix.

## 2.1 - Create an order

###Call

>```text
<market>/money/order/add
>```

###Request
>`type` string
```
'bid', 'ask'
```
___
`amount_int` int
```
Amount BTC, amount LTC (*1e8)
```
<span style="font-size: 12px">The field described above is optional</span>
___
`price_int` int
```
Limit price in EUR (*1e5)
```
<span style="font-size: 12px">The field described above is optional</span>
___
`amount_funds_int` int
```
Maximal EUR amount to spend (*1e5)
```
<span style="font-size: 12px">The field described above is optional</span>
___
`fee_currency` string
```
Currency the fee is accounted in. Can be: 'EUR' or 'BTC'
```
>___

###Response
>`order_id` int
```
The id of the order.
>```

## 2.2 - Cancel an order

###Call

>```text
<market>/money/order/cancel
>```

###Request
>`order_id` int
```
The id of the order that you wish to cancel.
>```

###Response
>```
For this call there is no specific result returned other then
the result of the call which contains: 'success' or 'failed' and a optional error array.
>```


## 2.3 - Get a specific order
###Call
>```text
<market>/money/order/result
>```

###Request
>`order_id` int
```
The id of the order that you wish to retrieve.
>```

###Response
>`order_id` int
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
The item that will be traded for `currency`. (Can be: 'BTC' or 'LTC')
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
<span style="font-size: 12px">The field described above is optional</span>
___
`price` amountObj
```
Order limit price.
```
<span style="font-size: 12px">The field described above is optional</span>
___
`status` string
```
Status of the order. (Can be: 'pending’, ‘open’, ‘closed’, ‘cancelled’)
```
___
`date` timestamp
```
The time the order got added.
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
<span style="font-size: 12px">The field described above is optional</span>
___
`trades` array
```
Array of trades executed for the regarding order.
```
**Each array item of 'trade' will contain:**
>>`amount` amountObj
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
'BTC' or 'LTC'
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
>>
>___

## 2.4 - Get the whole orderbook

###Call

>```text
<market>/money/depth/full
>```

###Request

>```
There are no specific parameters required for this call.
>```

###Response
>`asks` array
```
Array of asks that are in the orderbook.
```
**Each array item of 'asks' will contain:**

>>`amount_int` int
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
>>
>___

>`bids` array
```
Array of bids that are in the orderbook.
```
**Each array item of 'bids' will contain:**

>>`amount_int` int
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
>>
>___

## 3 - Account info & functions

## 3.1 - Get your transaction history

###Call

>```text
GENMKT/money/wallet/history
>```

###Request

>`currency` string
```
Currency of the wallet. (Can be: 'BTC', 'EUR' or 'LTC')
```
___
`page` int
```
Page number. (1 = most recent transactions)
```
<span style="font-size: 12px">The field described above is optional</span>
___
`date_from` timestamp
```
Filter the result by an Unix-timestamp. Transactions before this date will not be returned.
```
<span style="font-size: 12px">The field described above is optional</span>
___
`date_to` timestamp
```
Filter the result by an Unix-timestamp. Transactions after this date will not be returned.
```
<span style="font-size: 12px">The field described above is optional</span>
___
`type` string
```
Filter the result by type. (Can be: ‘trade’, ‘fee’, ‘deposit’, ‘withdraw’)
```
<span style="font-size: 12px">The field described above is optional</span>
___
`recs_per_page` int
```
Number of records per page.
```
<span style="font-size: 12px">The field described above is optional</span>
>___

###Response

>`page` int
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
>>`transaction_id` int
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
<span style="font-size: 12px">The field described above is optional</span>
___
`order_id` int
```
Id of the order.
```
<span style="font-size: 12px">The field described above is optional</span>
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
<span style="font-size: 12px">The field described above is optional</span>
___
`contra_amount` amountObj
```
Contra amount of the trade.
```
<span style="font-size: 12px">The field described above is optional</span>
___
`fee` amountObj
```
Fee incurred by the regarding trade
```
>>
>___

## 3.2 - Create a new deposit address

###Call

>```text
<market>/money/new_deposit_address
>```

###Request

>```
There are no specific parameters required for this call.
>```

###Response

>`address` string
```
Deposit address for the market leading currency
>```

## 3.3 - Get the last deposit address

###Call

>```text
<market>/money/deposit_address
>```

###Request

>```
There are no specific parameters required for this call.
>```

###Response

>`address` string
```
Deposit address for the market leading currency
>```

## 3.4 - Create a withdrawal

###Call

>```text
<market>/money/withdraw
>```

###Request
>`account_id` string
```
IBAN account-id (that is available within the regarding BL3P account)
>```
**or**

>`address` string
```
Bitcoin address
>```
___
>`amount_int` int
```
Satoshis or 0,00001 EUR
>```

###Response

>`id` int
```
Id of the withdrawal
>```

##3.5 - Get account info & balance
###Call

>```text
<market>/money/info
>```

###Request

>```
There are no specific parameters required for this call.
>```

###Response

>`user_id` int
```
Id of the user.
```
___
`trade_fee` float
```
Percentage fee for the user
```
___
`wallets` array
```
Array of wallets.
```
**Each array item of 'wallets' will contain:**

>>`balance` amountObj
```
Balance in this wallet
```
___
`available` amountObj
```
Available in this wallet.
```
>>
>___

##3.6 Get active orders
###Call
>```text
<market>/money/orders
>```

###Request

>```
There are no specific parameters required for this call.
>```

###Response

>`orders` array
```
Array of active orders.
```
**Each array item of 'orders' will contain:**

>>`order_id` int
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
The item that will be traded for `currency`. (Can be: 'BTC' or 'LTC')
```
___
`type` string
```
Type of order. (Can be: 'bid', 'ask')
```
___
`status` string
```
Status of the order. (Can be: 'pending’, ‘open’, ‘closed’, ‘cancelled’)
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
<span style="font-size: 12px">The field described above is optional</span>
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
<span style="font-size: 12px">The field described above is optional</span>
___
`amount_funds` amountObj
```
Maximal EUR amount to spend (*1e5)
```
<span style="font-size: 12px">The field described above is optional</span>
>>
>___

##3.7 - Get the last 1000 trades after an specific trade

###Call

>```text
<market>/money/trades/fetch
>```

###Request

>`trade_id` int
```
Id of the trade
```
The field described above is optional, if this field isn't specified, this call will return the last 1000 trades.
>

###Response

>`trades` array
```
Array of trades.
```
**Each array item of 'trades' will contain:**
>>`trade_id` int
```
Id of the trade.
```
___
`date` timestamp
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
>>
>___

## 4 - Appendix - Error codes

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