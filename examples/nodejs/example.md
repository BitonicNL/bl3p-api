# BL3P NodeJS module

## Table of contents

1. Introduction

  1. Installation
  2. Example code

2. Basic functions

  1. Create an order
  2. Cancel an order
  3. Get a specific order
  4. Get the whole orderbook
  5. Live trade stream
  6. Live orderbook stream

3. Account info & functions

  1. Get the transaction history
  2. Create a new deposit address
  3. Get the last deposit address
  4. Create a withdrawal
  5. Get account info & balance
  6. Get active orders
  7. Get the last 1000 trades after a specific trade

4. Appendix - Error code

---

## 1 - Introduction

This document describes the usage of BL3P NodeJS module.
If you don't have an API-key you can sign up and create one at https://bl3p.eu.

## 1.1 - Installation

The BL3P nodejs library is available within Node Package Manager.

https://www.npmjs.com/package/bl3p

To install, navigate into your nodejs project directory and run the defined command below in your command-line:
```
npm install bl3p
```

## 1.2 - Example code

```javascript
var bl3p = require('bl3p');
var public_key = 'YOUR_PUBLIC_KEY';
var private_key = 'YOUR_PRIVATE_KEY';

var bl3p_auth = new bl3p.Bl3pAuth(public_key, private_key);

bl3p_auth.account_info(function(error, data){
  if(data){
    console.log(data);
  }else{
    console.log(error);
  }
});

bl3p.trades(function(error, data){
  if(data){
    console.log(data);
  }else{
    console.log(error);
  }
});

bl3p.orderbook(function(error, data){
  if(data){
    console.log(data);
  }else{
    console.log(error);
  }
});
```

## 2 - Basic functions

All the methods return a data and an error array in JSON format.
All methods also require a callback method. The callback method is always the last required parameter.
In case of an error, an error code will be retuned. The possible error codes are listed in the appendix.

## 2.1 - Create an order

### Method

>```text
>add_order(amount, type, price, fee_currency, amount_funds, callback)
>```

### Parameters
>`type` string
>```
>'bid', 'ask'
>```
>___
>`amount` int
>```
>Amount BTC, amount LTC (*1e8)
>```
>The field described above is optional
>___
>`price` int
>```
>Limit price in EUR (*1e5)
>```
>The field described above is optional
>___
>`amount_funds` int
>```
>Maximal EUR amount to spend (*1e5)
>```
>The field described above is optional
>___
>`fee_currency` string
>```
>Currency the fee is accounted in. Can be: 'EUR' or 'BTC'
>```
>___

### Response
>`order_id` int
>```
>The id of the order.
>```

## 2.2 - Cancel an order

### Method

>```text
>cancel_order(order_id, callback)
>```

### Parameters
>`order_id` int
>```
>The id of the order that you wish to cancel.
>```

### Response
>```
>For this call there is no specific result returned other then
>the result of the call which contains: 'success' or 'failed' and a optional error array.
>```


## 2.3 - Get a specific order
### Method
>```text
>order_info(order_id, callback)
>```

### Parameters
>`order_id` int
>```
>The id of the order that you wish to retrieve.
>```

### Response
>`order_id` int
>```
>Id of the order.
>```
>___
>`label` string
>```
>API-key label
>```
>___
>`currency` string
>```
>Currency of the order. (Is now by default 'EUR')
>```
>___
>`item` string
>```
>The item that will be traded for `currency`. (Can be: 'BTC' or 'LTC')
>```
>___
>`type` string
>```
>Type of order. (Can be: 'bid', 'ask')
>```
>___
>`amount` amountObj
>```
>Total order amount of BTC or LTC.
>```
>The field described above is optional
>___
>`price` amountObj
>```
>Order limit price.
>```
>The field described above is optional
>___
>`status` string
>```
>Status of the order. (Can be: 'pending’, ‘open’, ‘closed’, ‘cancelled’)
>```
>___
>`date` timestamp
>```
>The time the order got added.
>```
>___
>`total_amount` amountObj
>```
>Total amount of the trades that got executed. (Can be: BTC or LTC).
>```
>___
>`total_spent` amountObj
>```
>Total amount in EUR of the trades that got executed.
>```
>___
>`total_fee` amountObj
>```
>Total fee incurred in BTC or LTC.
>```
>___
>`avg_cost` amountObj
>```
>Average cost of executed trades.
>```
>The field described above is optional
>___
>`trades` array
>```
>Array of trades executed for the regarding order.
>```
>**Each array item of 'trade' will contain:**
>>`amount` amountObj
>>```
>>BTC or LTC amount.
>>```
>>___
>>`currency` string
>>```
>>Currency of the regarding trade.
>>```
>>___
>>`date` timestamp
>>```
>>The time of the trade execution.
>>```
>>___
>>`item` string
>>```
>>'BTC' or 'LTC'
>>```
>>___
>>`price` amountObj
>>```
>>Price of the executed trade in EUR.
>>```
>>___
>>`trade_id` int
>>```
>>Id of trade.
>>```
>>
>___

## 2.4 - Get the whole orderbook

### Method

>```text
>full_depth(callback)
>```

### Parameters

>```
>There are no specific parameters required for this call.
>```

### Response
>`asks` array
>```
>Array of asks that are in the orderbook.
>```
>**Each array item of 'asks' will contain:**
>>
>>`amount_int` int
>>```
>>Amount BTC, amount LTC (*1e8)
>>```
>>___
>>`price_int` int
>>```
>>Limit price in EUR (*1e5)
>>```
>>___
>>`count` int
>>```
>>Count of orders at this price.
>>```
>>
>___
>>
>`bids` array
>```
>Array of bids that are in the orderbook.
>```
>**Each array item of 'bids' will contain:**
>>
>>`amount_int` int
>>```
>>Amount BTC, amount LTC (*1e8)
>>```
>>___
>>`price_int` int
>>```
>>Limit price in EUR (*1e5)
>>```
>>___
>>`count` int
>>```
>>Count of orders at this price.
>>```
>>
>___

## 2.5 - Live trade stream

###  Method

>```text
>trades(callback)
>```

###  Response

>`amount_int` int
>```
>Traded BTC Amount or  traded LTC amount (*1e8)
>```
>___
>`price_int` int
>```
>Trade price in EUR (*1e5)
>```
>___
>`date` timestamp
>```
>The time of the trade execution.
>```
___

## 2.6 - Live orderbook stream

###  Method

>```text
>orderbook(callback)
>```

### Response
>`asks` array
>```
>Array of asks that are in the orderbook.
>```
>**Each array item of 'asks' will contain:**
>
>>`amount_int` int
>>```
>>Amount BTC, amount LTC (*1e8)
>>```
>>___
>>`price_int` int
>>```
>>Limit price in EUR (*1e5)
>>```
>>___
>>`count` int
>>```
>>Count of orders at this price.
>>```
>>
>___
>
>`bids` array
>```
>Array of bids that are in the orderbook.
>```
>**Each array item of 'bids' will contain:**
>>
>>`amount_int` int
>>```
>>Amount BTC, amount LTC (*1e8)
>>```
>>___
>>`price_int` int
>>```
>>Limit price in EUR (*1e5)
>>```
>>___
>>`count` int
>>```
>>Count of orders at this price.
>>```
>>
>___

## 3 - Account info & functions

## 3.1 - Get your transaction history

### Method

>```text
>wallet_history(currency, page, date_from, date_to, type, recs_per_page, callback)
>```

### Parameters

>`currency` string
>```
>Currency of the wallet. (Can be: 'BTC', 'EUR' or 'LTC')
>```
>___
>`page` int
>```
>Page number. (1 = most recent transactions)
>```
>The field described above is optional
>___
>`date_from` timestamp
>```
>Filter the result by an Unix-timestamp. Transactions before this date will not be returned.
>```
>The field described above is optional
>___
>`date_to` timestamp
>```
>Filter the result by an Unix-timestamp. Transactions after this date will not be returned.
>```
>The field described above is optional
>___
>`type` string
>```
>Filter the result by type. (Can be: ‘trade’, ‘fee’, ‘deposit’, ‘withdraw’)
>```
>The field described above is optional
>___
>`recs_per_page` int
>```
>Number of records per page.
>```
>The field described above is optional
>___

### Response

>`page` int
>```
>Current page number.
>```
>___
>`records` int
>```
>Count of records in the result set.
>```
>___
>`max_page` int
>```
>Number of last page.
>```
>___
>`transactions` array
>```
>Array of transactions.
>```
>**Each array item of 'transactions' will contain:**
>>`transaction_id` int
>>```
>>Id of the transaction.
>>```
>>`amount` amountObj
>>```
>>BTC or LTC amount.
>>```
>>___
>>`date` timestamp
>>```
>>Time when the regarding transaction took place.
>>```
>>___
>>`debit_credit` string
>>```
>>Type of booking. (Can be: 'debit' or 'credit')
>>```
>>___
>>`price` amountObj
>>```
>>Price of the executed trade.
>>```
>>The field described above is optional
>>___
>>`order_id` int
>>```
>>Id of the order.
>>```
>>The field described above is optional
>>___
>>`type` string
>>```
>>Type of transaction (Can be: 'trade’, ‘fee’, ‘deposit’, ‘withdraw’)
>>```
>>___
>>`balance` amountObj
>>```
>>Balance of the user his account (for the regarding currency) after the transaction.
>>```
>>___
>>`trade_id` int
>>```
>>Id of the trade.
>>```
>>The field described above is optional
>>___
>>`contra_amount` amountObj
>>```
>>Contra amount of the trade.
>>```
>>The field described above is optional
>>___
>>`fee` amountObj
>>```
>>Fee incurred by the regarding trade
>>```
>>
>___

## 3.2 - Create a new deposit address

### Method

>```text
>new_deposit_address(callback)
>```

### Parameters

>```
>There are no specific parameters required for this call.
>```

### Response

>`address` string
>```
>Deposit address for the market leading currency
>```

## 3.3 - Get the last deposit address

### Method

>```text
>last_deposit_address
>```

### Parameters

>```
>There are no specific parameters required for this call.
>```

### Response

>`address` string
>```
>Deposit address for the market leading currency
>```

## 3.4 - Create a withdrawal

### Method

>```text
>withdraw(type, amount, account, callback)
>```

### Parameters
>`account` string
>```
>IBAN account-id (that is available within the regarding BL3P account) or a Bitcoin address
>```
>**Note: The kind of account value you need to specify depends on the 'type' parameter described below.**
>___
>`type` string
>```
>Can be 'EUR' or 'BTC'
>```
>___
>`amount` int
>```
>Satoshis or 0,00001 EUR
>```

### Response

>`id` int
>```
>Id of the withdrawal
>```

## 3.5 - Get account info & balance
### Method

>```text
>account_info(callback)
>```

### Parameters

>```
>There are no specific parameters required for this call.
>```

### Response

>`user_id` int
>```
>Id of the user.
>```
>___
>`trade_fee` float
>```
>Percentage fee for the user
>```
>___
>`wallets` array
>```
>Array of wallets.
>```
>**Each array item of 'wallets' will contain:**
>>
>>`balance` amountObj
>>```
>>Balance in this wallet
>>```
>>___
>>`available` amountObj
>>```
>>Available in this wallet.
>>```
>>
>___

## 3.6 Get active orders
### Method
>```text
>active_orders(callback)
>```

### Parameters

>```
>There are no specific parameters required for this call.
>```

### Response

>`orders` array
>```
>Array of active orders.
>```
>**Each array item of 'orders' will contain:**
>
>>`order_id` int
>>```
>>Id of the order.
>>```
>>___
>>`label` string
>>```
>>API-key label
>>```
>>___
>>`currency` string
>>```
>>Currency of the order. (Is now by default 'EUR')
>>```
>>___
>>`item` string
>>```
>>The item that will be traded for `currency`. (Can be: 'BTC' or 'LTC')
>>```
>>___
>>`type` string
>>```
>>Type of order. (Can be: 'bid', 'ask')
>>```
>>___
>>`status` string
>>```
>>Status of the order. (Can be: 'pending’, ‘open’, ‘closed’, ‘cancelled’)
>>```
>>___
>>`date` timestamp
>>```
>>The time the order got added.
>>```
>>___
>>`amount` amountObj
>>```
>>Total order amount of BTC or LTC.
>>```
>>The field described above is optional
>>___
>>`amount_funds_executed` amountObj
>>```
>>Amount in funds that is executed.
>>```
>>___
>>`amount_executed` amountObj
>>```
>>Amount that is executed.
>>```
>>___
>>`price` amountObj
>>```
>>Order limit price.
>>```
>>The field described above is optional
>>___
>>`amount_funds` amountObj
>>```
>>Maximal EUR amount to spend (*1e5)
>>```
>>The field described above is optional
>>
>___

## 3.7 - Get the last 1000 trades after a specific trade

### Method

>```text
>last_1000_trades(trade_id, callback)
>```

### Parameters

>`trade_id` int
>```
>Id of the trade
>```
>The field described above is optional, if this field isn't specified, this call will return the last 1000 trades.
>

### Response

>`trades` array
>```
>Array of trades.
>```
>**Each array item of 'trades' will contain:**
>>`trade_id` int
>>```
>>Id of the trade.
>>```
>>___
>>`date` timestamp
>>```
>>The time of the trade execution.
>>```
>>___
>>`amount_int` int
>>```
>>Amount traded. (*1e8)
>>```
>>___
>>`price_int` int
>>```
>>Price of the traded item in EUR. (*1e5)
>>```
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
