import csv

withdrawn_transactions = []
adjustment_transactions = []
trade_transactions = []
deposit_transactions = []
with open("account-history-2021-Apinan_Yogaratnam.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        