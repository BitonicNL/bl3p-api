# Public API | REST Calls

## Table of contents

1. Introduction
2. Basic functions

  1. Ticker

## 1 - Introduction

This document describes the usage of the public REST API of BL3P.
In the file on directory above you can find the base.md file.
The base.md document describes all basic details that you need to know to use the BL3P API.
If you would like to know how to make a connection to the BL3P API, please check the examples that are available one directory above.

## 2. Basic functions

**Definition of the path variable:**
```
/<market>
```
___
**Description of the path variable:**

___
Market that the call will be applied to.

```
<market> = ‘BTCEUR’, 'LTCEUR'
```
___

## 2.1 - Ticker

###Request

>```
There are no specific parameters required for this call.
>```

###Response

>`currency` string
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
>>`24h` float
```
Volume of the last 24 hours.
```
___
`30d` float
```
Volume of the last 30 days.
```
>>
>___