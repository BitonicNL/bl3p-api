package main

import (
	"fmt"
	"time"

	bl3p "github.com/dfijma/bl3p-api/examples/go/bl3p"
)

func main() {

	var bl3p = bl3p.NewBl3p(
		"https://api.bl3p.eu",
		"YOUR_PUBLIC_API_KEY",
		"YOUR_PRIVATE_API_KEY",
		"1",
	)

	depositAddress, err := bl3p.GetNewDepositAddress()
	if err != nil {
		panic(err)
	} else {
		fmt.Println(depositAddress)
	}

	last1000trades, err := bl3p.FetchLast1000Trades(0)
	if err != nil {
		fmt.Println(err)
	} else {
		var dayvol float64
		for _, t := range last1000trades.Trade {
			if int32(t.Date/1000) >= int32(time.Now().Unix()-86400) {
				amountPrice := float64(t.AmountInt) / 1e8
				dayvol = dayvol + amountPrice
			}
		}
		fmt.Printf("The volume of the last 24 hours is: %v \n", dayvol)
	}
}
