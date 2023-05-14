' Coded by Foen1337@gmail.com 
' it has been released under AGPL v3.0
' it requires "Flurl https://tmenier.github.io/Flurl/"

Imports System.Security.Cryptography
Imports Flurl
Imports Flurl.Http

Friend Class Bl3p_PrivateApi
    'base Url to bl3p
    Dim host As String = "https://api.bl3p.eu/1/"
    Public publickey As String
    Public privatekey As String

    'Fetch complete orderbook 
    Public Function fullDepth(ByVal currency As String) As String
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/depth/full")
        Return json
    End Function

    'Get balance for all wallets
    Public Function wallets() As String
        'call bl3p api and return its json
        Dim json As String = ApiCall("GENMKT/money/info")
        Return json
    End Function

    'create new deposit address.
    Public Function getNewDepositAddress(ByVal currency As String) As String
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/new_deposit_address")
        Return json
    End Function

    'Add order to your account.
    Public Function addOrder(ByVal currency As String, ByVal type As String, ByVal amount_int As Int32, ByVal price_int As Int32, ByVal fee_currency As String) As String
        Dim parameters = New List(Of KeyValuePair(Of String, String))()
        parameters.Add(New KeyValuePair(Of String, String)("type", type))
        parameters.Add(New KeyValuePair(Of String, String)("amount_int", amount_int * 100000000.0))
        parameters.Add(New KeyValuePair(Of String, String)("price_int", price_int * 100000.0))
        parameters.Add(New KeyValuePair(Of String, String)("fee_currency", fee_currency.ToUpper))
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/order/add", parameters)
        Return json
    End Function

    'Fetch complete orderbook
    Public Function orderInfo(ByVal currency As String, ByVal orderid As String) As String
        Dim parameters = New List(Of KeyValuePair(Of String, String))()
        parameters.Add(New KeyValuePair(Of String, String)("order_id", orderid))
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/order/result", parameters)
        Return json
    End Function

    'cancel order
    Public Function cancelOrder(ByVal currency As String, ByVal orderid As String) As String
        Dim parameters = New List(Of KeyValuePair(Of String, String))()
        parameters.Add(New KeyValuePair(Of String, String)("order_id", orderid))
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/order/cancel", parameters)
        Return json
    End Function

    'Get all open orders.
    Public Function getAllActiveOrders(ByVal currency As String) As String
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/orders")
        Return json
    End Function

    'Get the most recent generated deposit address
    Public Function getLastDepositAddress(ByVal currency As String) As String
        'call bl3p api and return its json
        Dim json As String = ApiCall(currency.ToUpper & "EUR/money/deposit_address")
        Return json
    End Function

    'Get the transaction history
    Public Function walletHistory(ByVal currency As String, ByVal type As String, ByVal pages As Integer) As String
        'create the POST parameters list needed for the wallet history [currency] [recs_per_page] 
        Dim parameters = New List(Of KeyValuePair(Of String, String))()
        'create new parameter and add to list
        parameters.Add(New KeyValuePair(Of String, String)("currency", currency.ToUpper))
        parameters.Add(New KeyValuePair(Of String, String)("recs_per_page", pages))
        parameters.Add(New KeyValuePair(Of String, String)("type", type)) ' filter (Can be: ‘trade’, ‘fee’, ‘deposit’, ‘withdraw’)
        'call bl3p api and return its json
        Dim json As String = ApiCall("GENMKT/money/wallet/history", parameters)
        Return json

    End Function

    Private Function ApiCall(ByVal path As String, Optional parameters As List(Of KeyValuePair(Of String, String)) = Nothing) As String
        Try

            'make timestamp in milisecs
            Dim timestamp = Math.Round((Date.Now.ToUniversalTime() - New Date(1970, 1, 1)).Ticks)

            'check if there are any parameters passed to the api 
            If parameters Is Nothing Then
                ' if no parameters pass create list 
                parameters = New List(Of KeyValuePair(Of String, String))()
            End If
            ' add nonce to all calls 
            parameters.Add(New KeyValuePair(Of String, String)("nonce", timestamp))

            'build POST parameters
            Dim parameterURl As String = ""
            For Each key In parameters
                'for each key add to url
                parameterURl += key.Key & "=" & key.Value & "&"
            Next
            'trim last & from parameter URL
            parameterURl = parameterURl.TrimEnd("&")

            'make a message to send
            Dim message = path & vbNullChar & parameterURl
            'create the Rest signature
            Dim signature = CreateSignature(message, privatekey)
            'call the api and get response
            Dim coinbasewalletinfo = host.AppendPathSegments(path).WithHeader("Content-Type", "application/json").WithHeader("Rest-Key", publickey).WithHeader("Rest-Sign", signature).PostUrlEncodedAsync(parameters).ReceiveJson(Of Object)().Result

            'print response
            Return coinbasewalletinfo.ToString
        Catch ex As Exception
            'get error message 
            Dim errormessagefull As String = ex.InnerException.Message
            'get json from the error message and pass it tru
            Dim errorJson As String = errormessagefull.Substring(errormessagefull.IndexOf("{"c))
            Return errorJson
        End Try

    End Function

    Private Function CreateSignature(ByVal message As String, ByVal key As String) As String
        'decode the key with base64
        Dim Decodedkey() As Byte = Convert.FromBase64String(key)
        'get message as byte
        Dim encoding = New System.Text.UTF8Encoding()
        Dim messageBytes() As Byte = encoding.GetBytes(message)
        'make HMACSHA512
        Using hmacsha1 = New HMACSHA512(Decodedkey)
            'compute hash with decoded key
            Dim hashmessage() As Byte = hmacsha1.ComputeHash(messageBytes)
            'return base64 encoded string
            Return Convert.ToBase64String(hashmessage)
        End Using
    End Function


End Class
