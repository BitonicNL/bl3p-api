# Public API | Websocket Calls

## Table of contents

1. Introduction
2. Basic functions
  1. Trades
  2. Orderbook

## 1 - Introduction

This document describes the usage of the public websocket API of BL3P.
In the file on directory above you can find the base.md file.
The base.md document describes all basic details that you need to know to use the BL3P API.
If you would like to know how to make a connection to the BL3P API, please check the examples that are available one directory above.

## 2. Basic functions

**Definition of the path variables:**
```
/<version>/<market>/<channel>
```
___
**Description of the path variables:**

Version of API (is currently: 1)
```
<version> = 1
```
___
Market that the call will be applied to.

```
<market> = ‘BTCEUR’, 'LTCEUR'
```
___
Channel to subscribe to.
```
<channel> = $channel_name
```
___

## 2.1 - Trades

### Channel
`trades` string

```
The 'trades' ticker streams trade messages to subscribers.
```

### Message

`amount_int` int
```
Traded BTC Amount or  traded LTC amount (*1e8)
```
___
`price_int` int
```
Trade price in EUR (*1e5)
```
___
`date` timestamp
```
The time of the trade execution.
```
___


## 2.2 - Orderbook

### Channel
`orderbook` string
```
The 'orderbook' ticker streams the orderbook to subscribers, every time a change occurs.
```

### Message

`asks` array
```
Array of asks that are in the orderbook.
```
**Each array item of 'asks' will contain:**

>`amount_int` int
>```
>BTC amount or LTC amount (*1e8)
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
>
>___

`bids` array
```
Array of bids that are in the orderbook.
```
**Each array item of 'bids' will contain:**

>`amount_int` int
>```
>BTC amount or LTC amount (*1e8)
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
>
>___
