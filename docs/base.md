# Base

## Table of contents

1. Introduction
2. General information

  1. Public API & Authenticated API
  2. Base urls
  3. Authentication and authorization
  4. Capacity
  5. AmountObj type

---

## 1 - General information

### 2.1 - Public API & Authenticated API

There are two different API types.
A Public API and an Authenticated API.
The Public API will supply basic public information like all trades and the orderbook.
The Authenticated API differs from the Public API since you can control your BL3P account and retrieve non-public information about your BL3P account.

### 2.2 - Base urls

The base urls for the two different APIs are as following:

###Authenticated API

**HTTP**
```
https://api.bl3p.eu
```
___
###Public API

**Websocket**
```
wss://api.bl3p.eu/
```
**HTTP**
```
https://api.bl3p.eu
```
___

### 2.3 Authentication and authorization

On the [security page](https://www.bl3p.eu/security) within BL3P you can add one or more API keys.
Use this API key to control your BL3P account.
For the Public API this API key is not required.

The Authenticated API requires two variables to be passed within the HEADER.

`Rest-Key`

This is contains the raw API key.
___
`Rest-Sign`

You also need to sign the Rest-Key. This variable needs to contain the following:
```
base64 encode of (
	HMAC_SHA512 of (
		$path_of_request + null terminator + $post_data_string
	) with the key set to the base64 decode of the private apikey)
)
```
Note: That the HMAC_SHA512 needs to output raw binary data, using hexits (hexadecimal digits) will return an error.

### 2.4 - Capacity

You cannot call the API unlimited times in a certain timeframe.
The current amount of calls per 10 minutes is set to 600.

### 2.5 - AmountObj type

You will notice that sometimes we don't define an field type as '_string_', '_array_' or '_int_', but as '_amountObj_'.
This is an type of field which will always maintain the following format:

`value_int` string

The amount in 1e5 (for fiat) or 1e8 (for virtual currency).

**Example:**
```
100000
```
___
`display_short` string

The common notation of this amount.

**Example:**
```
1.00 EUR
```
___
`display` string

The amount in 1e5 (for fiat) or 1e8 (for virtual currency), with decimal notation and the regarding currency.

**Example:**
```
1.00000 EUR
```
___
`currency` string

The currency of the amountObj.

**Example:**
```
'EUR'
```
___
`value` string

The amount in 1e5 (for fiat) or 1e8 (for virtual currency), with decimal notation.

**Example:**
```
1.00000
```
