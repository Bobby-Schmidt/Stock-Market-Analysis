import sqlite3 as lite
import sys
import ystockquote as stock
from time import strftime, sleep
from prettytable import PrettyTable

#	Connect to the database
con = lite.connect('Stock.db')

#	Declaration of Stock Symbols
ticker_sym_aapl = 'AAPL'
ticker_sym_egy = 'EGY'
ticker_sym_vde = 'VDE'
ticker_sym_tsla = 'TSLA'

id_val = 0

with con:

	while True:
		cur = con.cursor()

		quote_time = strftime("%Y-%m-%d %H:%M:%S")

		stock_quote_aapl = stock.get_price(ticker_sym_aapl)
		stock_quote_egy = stock.get_price(ticker_sym_egy)
		stock_quote_vde = stock.get_price(ticker_sym_vde)
		stock_quote_tsla = stock.get_price(ticker_sym_tsla)

		table = PrettyTable(["Ticker Symbol", "Price Quote"])
		table.add_row([ticker_sym_aapl, stock_quote_aapl])
		table.add_row([ticker_sym_egy, stock_quote_egy])
		table.add_row([ticker_sym_vde, stock_quote_vde])
		table.add_row([ticker_sym_tsla, stock_quote_tsla])
		table.add_row(["-","-"])
		table.add_row(["Quote Time", quote_time])

		print table

		apple_data = (
				(id_val, quote_time, stock_quote_aapl)
			)

		vaalco_data = (
				(id_val, quote_time, stock_quote_egy)
			)

		vanguardEnergy_data = (
				(id_val, quote_time, stock_quote_vde)
			)

		tesla_data = (
				(id_val, quote_time, stock_quote_tsla)
			)


		cur.executemany("INSERT INTO Apple VALUES(?, ?, ?)", (apple_data,))
		cur.executemany("INSERT INTO Vaalco VALUES(?, ?, ?)", (vaalco_data,))
		cur.executemany("INSERT INTO VanguardEnergy VALUES(?, ?, ?)", (vanguardEnergy_data,))
		cur.executemany("INSERT INTO Tesla VALUES(?, ?, ?)", (tesla_data,))

		id_val = id_val + 1

		sleep(60)
