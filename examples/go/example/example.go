package main

import (
	"fmt"
	"projects/bl3pgo/bl3p"
	"time"
)

func main() {
	result, err := bl3p.FetchLast1000Trades(0)
	if err != nil {
		fmt.Println(err)
	} else {
		var dayvol float64
		for _, t := range result.Trade {
			if int32(t.Date/1000) >= int32(time.Now().Unix()-86400) {
				amountPrice := float64(t.AmountInt) / 1e8
				dayvol = dayvol + amountPrice
			}
		}
		fmt.Printf("The volume of the last 24 hours is: %v \n", dayvol)
	}
}
