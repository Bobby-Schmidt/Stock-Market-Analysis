import ystockquote as stock
from time import strftime, sleep
from prettytable import PrettyTable



#	Declaration of Stock Symbols
ticker_sym_aapl = 'AAPL'
ticker_sym_egy = 'EGY'
ticker_sym_vde = 'VDE'
ticker_sym_tsla = 'TSLA'


while True:

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

	# print "---------------------------------------"
	# print "Quote Time: %s \n" % strftime("%Y-%m-%d %H:%M:%S")

	# print "Current Apple Price: %s" % stock.get_price(ticker_sym_aapl)
	# print "Current Vaalco Price: %s" % stock.get_price(ticker_sym_egy)
	# print "Current Vanguard Energy Price: %s" % stock.get_price(ticker_sym_vde)
	# print "Current Tesla Price: %s" % stock.get_price(ticker_sym_tsla)
	


	sleep(10)


