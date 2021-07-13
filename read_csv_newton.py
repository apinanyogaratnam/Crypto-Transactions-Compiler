import csv

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


# newton csv format
# Date | Type | Received Quantity | Receieved Currency | Set Quantity | Sent Currency | Fee Amount | Fee Currency | Tag

# trades
purchase_total_bitcoin = 0.0
bitcoin_received = 0.0
purchase_total_ethereum = 0.0
ethereum_received = 0.0
purchase_total_usdc = 0.0
usdc_received = 0.0
purchase_total_litecoin = 0.0
litecoin_received = 0.0

for transaction in trade_transactions:
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

print("Total spent on bitcoin: ", purchase_total_bitcoin)
print("Total bitcoin received: ", bitcoin_received)

print("Total spent on ethereum: ", purchase_total_ethereum)
print("Total ethereum received: ", "{:.9f}".format(ethereum_received))

print("Total spent on litecoin: ", purchase_total_litecoin)
print("Total litecoin received: ", litecoin_received)
