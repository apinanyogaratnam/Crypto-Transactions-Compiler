from read_csv_shakepay import *
from read_csv_newton import *

newton_data = get_data_newton()
newton_trade_transactions = newton_data[2]

newton_purchase_data = get_purchases_newton(newton_trade_transactions)
purchase_total_bitcoin = purchase_data[0]
bitcoin_received = purchase_data[1]
purchase_total_ethereum = purchase_data[2]
ethereum_received = purchase_data[3]
purchase_total_litecoin = purchase_data[4]
litecoin_received = purchase_data[5]
purchase_total_usdc = purchase_data[6]
usdc_received = purchase_data[7]

shakepay_data = get_data_shakepay()
shakepay_purchase_transactions = shakepay_data[1]

shakepay_purchase_data = get_purchases_shakepay(shakepay_purchase_transactions)
purchase_total_bitcoin = shakepay_purchase_data[0]
bitcoin_received = shakepay_purchase_data[1]
purchase_total_ethereum = shakepay_purchase_data[2]
ethereum_received = shakepay_purchase_data[3]