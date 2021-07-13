from read_csv_shakepay import *
from read_csv_newton import *

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

shakepay_data = get_data_shakepay()
shakepay_purchase_transactions = shakepay_data[1]

shakepay_purchase_data = get_purchases_shakepay(shakepay_purchase_transactions)
shakepay_purchase_total_bitcoin = shakepay_purchase_data[0]
shakepay_bitcoin_received = shakepay_purchase_data[1]
shakepay_purchase_total_ethereum = shakepay_purchase_data[2]
shakepay_ethereum_received = shakepay_purchase_data[3]

total_spent_on_bitcoin = newton_purchase_total_bitcoin + shakepay_purchase_total_bitcoin
total_bitcoin_received = newton_bitcoin_received + shakepay_bitcoin_received

total_spent_on_ethereum = newton_purchase_total_ethereum + shakepay_purchase_total_ethereum
total_ethereum_received = newton_ethereum_received + shakepay_ethereum_received

print("Total spent on bitcoin: ", total_spent_on_bitcoin)
print("Total bitcoin received: ", total_bitcoin_received)

print("Total spent on ethereum: ", total_spent_on_ethereum)
print("Total ethereum received: ", "{:.9f}".format(total_ethereum_received))

print("Loading...", end="\r")
current_value_of_your_bitcoin = convert_btc_to_cad(total_bitcoin_received)
profit_of_your_bitcoin = current_value_of_your_bitcoin - total_spent_on_bitcoin
percent_gains_of_your_bitcoin = round(profit_of_your_bitcoin / total_spent_on_bitcoin * 100, 2)
print("Current value of your bitcoin: ", current_value_of_your_bitcoin)
print("Profit/Loss of your bitcoin: : ", current_value_of_your_bitcoin - total_spent_on_bitcoin)
print("Percentage up/down of your bitcoin: ",  percent_gains_of_your_bitcoin, "%")

print("Loading...", end="\r")
current_value_of_your_ethereum = convert_eth_to_cad(total_ethereum_received)
profit_of_your_ethereum = current_value_of_your_ethereum - total_spent_on_ethereum
percent_gains_of_your_ethereum = round(profit_of_your_ethereum / total_spent_on_ethereum * 100, 2)
print("Current value of your ethereum: ", current_value_of_your_ethereum)
print("Profit/Loss of your ethereum: : ", profit_of_your_ethereum)
print("Percentage up/down of your ethereum: ", percent_gains_of_your_ethereum, "%")
