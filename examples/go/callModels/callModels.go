package callModels

import "encoding/json"

//Bl3pResult | Main result struct
type Bl3pResult struct {
	Result string          `json:"result"`
	Data   json.RawMessage `json:"data"`
}

//Fulldepth | FullDepth call struct
type Fulldepth struct {
	Bids []OrderbookItem
	Asks []OrderbookItem
}

//OrderbookItem | Orderbook item struct
type OrderbookItem struct {
	Count     int   `json:"count"`
	PriceInt  int64 `json:"price_int"`
	AmountInt int64 `json:"amount_int"`
}

//Orders | Order array struct
type Orders struct {
	Order []Order `json:"orders"`
}

//Trades | Trades array struct
type Trades struct {
	Trade []Trade `json:"trades"`
}

//Order | Order struct
type Order struct {
	OrderID             int64     `json:"order_id"`
	Label               string    `json:"label"`
	Currency            string    `json:"currency"`
	Item                string    `json:"item"`
	Type                string    `json:"type"`
	Status              string    `json:"status"`
	Date                int64     `json:"date"`
	Amount              AmountObj `json:"amount"`
	AmountExecuted      AmountObj `json:"amount_executed"`
	AmountFunds         AmountObj `json:"amount_funds"`
	AmountFundsExecuted AmountObj `json:"amount_funds_executed"`
	Price               AmountObj `json:"price"`
	TotalAmount         AmountObj `json:"total_amount"`
	TotalSpent          AmountObj `json:"total_spent"`
	TotalFee            AmountObj `json:"total_fee"`
	AvgCost             AmountObj `json:"avg_cost"`
	Trades              []Trade   `json:"trades"`
}

//Trade | Trade struct
type Trade struct {
	TradeID   int64     `json:"trade_id"`
	Date      int64     `json:"date"`
	Currency  string    `json:"currency"`
	Amount    AmountObj `json:"amount"`
	Price     AmountObj `json:"price"`
	AmountInt int64     `json:"amount_int"`
	Item      string    `json:"item"`
	PriceInt  int64     `json:"price_int"`
}

//AmountObj | AmountObj struct
type AmountObj struct {
	ValueInt     string `json:"value_int"`
	DisplayShort string `json:"display_short"`
	Display      string `json:"display"`
	Currency     string `json:"currency"`
	Value        string `json:"value"`
}

//DepositAddress | DepositAddress call struct
type DepositAddress struct {
	Address string `json:"address"`
}

//Transactions | WalletHistory call struct
type Transactions struct {
	Page         int64         `json:"page"`
	Records      int64         `json:"records"`
	MaxPpage     int64         `json:"max_page"`
	Transactions []Transaction `json:"transactions"`
}

//Transaction | Transaction struct
type Transaction struct {
	TransactionID int64     `json:"transaction_id"`
	Amount        AmountObj `json:"amount"`
	Date          int64     `json:"date"`
	DebitCredit   string    `json:"debit_credit"`
	Price         AmountObj `json:"price"`
	OrderID       int64     `json:"order_id"`
	Type          string    `json:"type"`
	Balance       AmountObj `json:"balance"`
	TradeID       int64     `json:"trade_id"`
	ContraAmount  AmountObj `json:"contra_amount"`
	Fee           AmountObj `json:"fee"`
}

//AddOrder | AddOrder call struct
type AddOrder struct {
	OrderID int64 `json:"order_id"`
}

//Wallet | Wallet struct
type Wallet struct {
	Balance   AmountObj `json:"balance"`
	Available AmountObj `json:"available"`
}

//Info | Account call struct
type Info struct {
	UserID  int64             `json:"user_id"`
	Wallets map[string]Wallet `json:"wallets"`
}
