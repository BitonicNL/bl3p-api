# Public API | HTTP Calls

## Table of contents

1. Introduction
2. Basic functions

  1. Ticker
  2. Orderbook
  3. Last 1000 trades
  4. Chart

## 1 - Introduction

This document describes the usage of the public HTTP API of BL3P.
In the file one directory above you can find the base.md file.
The base.md document describes all basic details that you need to know to use the BL3P API.
If you would like to know how to make a connection to the BL3P API, please check the examples that are available one directory above.

## 2. Basic functions

**Definition of the path variable:**
```
/<version>/<market>/<callname>
```
___
**Description of the path variable:**

___
Market that the call will be applied to.

```
<market> = ‘BTCEUR’
```

Version of API (is currently: 1)
```text
<version> = 1
```

___
Name of call (for example: “trades”)
```text
<callname> = $callname
```
___

## 2.1 - Ticker

### Call

```text
ticker
```
### Request

```
There are no specific parameters required for this call.
```
### Response

`currency` string
```
The currency the returned values apply to.
```
___
`last` float
```
Price of the last trade.
```
___
`bid` float
```
Price of the current bid.
```
___
`ask` float
```
Price of the current ask.
```
___
`volume` array
```
Array of trades executed for the regarding order.
```
**The 'volume' array will contain:**
>`24h` float
>```
>Volume of the last 24 hours.
>```
>___
>`30d` float
>```
>Volume of the last 30 days.
>```
>___

## 2.2 - Orderbook

### Call

```text
orderbook
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
**Each array item of 'asks' will contain:**

>`amount_int` int
>```
>Amount BTC (*1e8)
>```
>___
>`price_int` int
>```
>Limit price in EUR (*1e5)
>```
>___
>`count` int
>```
>Count of orders at this price.
>```
>___

`bids` array
```
Array of bids that are in the orderbook.
```
**Each array item of 'bids' will contain:**

>`amount_int` int
>```
>Amount BTC (*1e8)
>```
>___
>`price_int` int
>```
>Limit price in EUR (*1e5)
>```
>___
>`count` int
>```
>Count of orders at this price.
>```
>___

## 2.3 - Last 1000 trades

### Call

```text
trades
```

### Request

```
There are no specific parameters required for this call.
```

### Response

`trades` array
```
Array of trades.
```
**Each array item of 'trades' will contain:**
>`trade_id` int
>```
>Id of the trade.
>```
>___
>`date` timestamp (in milliseconds)
>```
>The time of the trade execution.
>```
>___
>`amount_int` int
>```
>Amount traded. (*1e8)
>```
>___
>`price_int` int
>```
>Price of the traded item in EUR. (*1e5)
>```
>___

## 2.4 - Chart

### Call

```text
tradehistory
```

### Request
`timefactor` string
```
'h', 'd', 'm', 'y'
```
The field described above is optional and if set, the timevalue parameter needs to be set as well
___
`timevalue` int
```
24
```
The field described above is optional and if set, the timefactor parameter needs to be set as well
>___

### Response

`tradehistory` array
```
An array containing datapoints
```
___

**The 'tradehistory' array will contain:**
>`t` float
>```
>The time of the datapoint
>```
>___
>`p` float
>```
>The price of the datapoint
>```
>___
>`v` float
>```
>The volume of the datapoint
>```
>___