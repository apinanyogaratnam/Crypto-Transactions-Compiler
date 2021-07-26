import csv

def get_data_newton():
    withdrawn_transactions = []
    adjustment_transactions = [] # seems unnecessary for now
    trade_transactions = []
    deposit_transactions = []
    with open("account-history-2021-Apinan_Yogaratnam.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if (row[1] == "TRADE"):
                trade_transactions.append(row)
            elif (row[1] == "WITHDRAWN"):
                withdrawn_transactions.append(row)
            elif (row[1] == "DEPOSIT"):
                deposit_transactions.append(row)
    
    return (withdrawn_transactions, adjustment_transactions, trade_transactions, deposit_transactions)


# newton csv format
# Date | Type | Received Quantity | Receieved Currency | Set Quantity | Sent Currency | Fee Amount | Fee Currency | Tag

def get_purchases_newton(transactions):
    # trades
    purchase_total_bitcoin = 0.0
    bitcoin_received = 0.0

    purchase_total_ethereum = 0.0
    ethereum_received = 0.0

    purchase_total_usdc = 0.0
    usdc_received = 0.0

    purchase_total_litecoin = 0.0
    litecoin_received = 0.0

    for transaction in transactions:
        received_currency = transaction[3]
        sent_currency = transaction[5] # need to use this in our caluclation somehow after
        # as of now, assumed if received is btc, eth, ltc, sent is cad
        if (received_currency == "BTC"):
            bitcoin_received += float(transaction[2])
            purchase_total_bitcoin += float(transaction[4])
        elif (received_currency == "ETH"):
            ethereum_received += float(transaction[2])
            purchase_total_ethereum += float(transaction[4])
        elif (received_currency == "LTC"): 
            litecoin_received += float(transaction[2])
            purchase_total_litecoin += float(transaction[4])
        elif (received_currency == "USDC"):
            continue
        elif (received_currency == "CAD"):
            continue
    
    return (purchase_total_bitcoin, bitcoin_received, purchase_total_ethereum, ethereum_received, purchase_total_litecoin, litecoin_received, purchase_total_usdc, usdc_received)


if __name__ == '__main__':
    newton_data = get_data_newton()
    newton_trade_transactions = newton_data[2]

    newton_purchase_data = get_purchases_newton(newton_trade_transactions)
    newton_purchase_total_bitcoin = newton_purchase_data[0]
    newton_bitcoin_received = newton_purchase_data[1]
    newton_purchase_total_ethereum = newton_purchase_data[2]
    newton_ethereum_received = newton_purchase_data[3]
    newton_purchase_total_litecoin = newton_purchase_data[4]
    newton_litecoin_received = newton_purchase_data[5]
    newton_purchase_total_usdc = newton_purchase_data[6]
    newton_usdc_received = newton_purchase_data[7]

    total_spent_on_bitcoin = newton_purchase_total_bitcoin
    total_bitcoin_received = newton_bitcoin_received

    total_spent_on_ethereum = newton_purchase_total_ethereum
    total_ethereum_received = newton_ethereum_received

    print("Total spent on bitcoin: ", total_spent_on_bitcoin)
    print("Total bitcoin received: ", total_bitcoin_received)

    print("Total spent on ethereum: ", total_spent_on_ethereum)
    print("Total ethereum received: ", "{:.9f}".format(total_ethereum_received))
