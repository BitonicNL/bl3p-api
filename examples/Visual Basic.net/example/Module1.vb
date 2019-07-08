Module Module1

    Sub Main()
        Dim Bl3p As New Bl3p_PrivateApi With {.publickey = "", .privatekey = ""}
        ' Console.WriteLine(Bl3p.walletHistory("LTC", 25))
        'Console.WriteLine(Bl3p.getLastDepositAddress("LTC"))
        Console.WriteLine(Bl3p.fullDepth("LTC"))
        Console.ReadKey()
    End Sub

End Module
