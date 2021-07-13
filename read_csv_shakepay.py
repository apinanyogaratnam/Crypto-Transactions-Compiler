import csv
# import requests, json

#file_name = input("Enter file name with extension: ")

def get_data_shakepay():
    fiat_fundings = []
    purchase_sales = [] # complete
    peer_transfers = [] # complete (except actual peer transfers)
    referral_rewards = []
    crypto_cashouts = []

    with open("transactions_summary.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            if (row[0] == "peer transfer"): # assuming peer transfers are shaking sats only (for now)
                peer_transfers.append(row)
            elif (row[0] == "purchase/sale"):
                purchase_sales.append(row)
            elif (row[0] == "fiat funding"):
                fiat_fundings.append(row)
            elif (row[0] == "referral reward"):
                referral_rewards.append(row)
            elif (row[0] == "crypto cashout"):
                crypto_cashouts.append(row)
    
    return (fiat_fundings, purchase_sales, peer_transfers, referral_rewards, crypto_cashouts)

# shakepay csv format:
# Transaction Type | Date | Amount Debited | Debit Currency | Amount Credited | Credit Currency | Buy/Sell rate | Credit/Debit | Spot Rate | Address | Blockchain Transaction ID

def calculate_shakin_sats(transactions):
    count = 0.0
    for transaction in transactions:
        count += float(transaction[4])
    
    return (count, """convert_btc_to_cad(count)""")


# def convert_btc_to_cad(number_of_bitcoins):
#     response = requests.get("https://api.shakepay.co/rates")
#     response = response.json()
#     data = response
#     btc_cad = data['BTC_CAD']

#     return btc_cad * number_of_bitcoins
    

def get_purchases_shakepay(transactions):
    purchase_total_bitcoin = 0.0
    bitcoin_received = 0.0
    purchase_total_ethereum = 0.0
    ethereum_received = 0.0

    for sale in transactions:
        if ("," in sale[2]): sale[2] = sale[2].replace(",", "")
        if (sale[5] == "BTC"):
            purchase_total_bitcoin += float(sale[2])
            bitcoin_received += float(sale[4])
        elif (sale[5] == "ETH"):
            purchase_total_ethereum += float(sale[2])
            ethereum_received += float(sale[4])
    
    # returning (total spent on bitcoin, total bitcoin received from purchase, total spent on ethereum, total ethereum receieved from purchase)
    return (purchase_total_bitcoin, bitcoin_received, purchase_total_ethereum, ethereum_received)


# purchases = get_purchases_shakepay(purchase_sales)
# print("Total spent on Bitcoin: ", purchases[0])
# print("Amount of bitcoin received: ", purchases[1])

# print("Total spent on Ethereum: ", purchases[2])
# print("Amount of Ethereum received: ", purchases[3])