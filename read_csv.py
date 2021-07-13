import csv
# import requests, json

#file_name = input("Enter file name with extension: ")

fiat_fundings = []
purchase_sales = []
peer_transfers = []
referral_rewards = []
crypto_cashouts = []
shaking_sats_transactions = []



with open("transactions_summary.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
        if (row[0] == "peer transfer"): # assuming peer transfers are shaking sats only (for now)
            shaking_sats_transactions.append(row)
        if (row[0] == "purchase/sale"):
            purchase_sales.append(row)
        if (row[0] == "fiat funding"):
            fiat_fundings.append(row)
        if (row[0] == "referral reward"):
            referral_rewards.append(row)
        if (row[0] == "crypto cashout"):
            crypto_cashouts.append(row)

# shakepay csv format:
# Transaction Type | Date | Amount Debited | Debit Currency | Amount Credited | Credit Currency | Buy/Sell rate | Credit/Debit | Spot Rate | Address | Blockchain Transaction ID

def calculate_shakin_sats(transactions):
    count = 0.0
    for transaction in transactions:
        count += float(transaction[4])
    
    return (count, convert_btc_to_cad(count))


# def convert_btc_to_cad(number_of_bitcoins):
#     response = requests.get("https://api.shakepay.co/rates")
#     response = response.json()
#     data = response
#     btc_cad = data['BTC_CAD']

#     return btc_cad * number_of_bitcoins

# print(calculate_shakin_sats(shaking_sats_transactions))
