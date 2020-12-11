import analysis.stockViewer as sv
import analysis.candleRecognition as cr

def main():
	ticker = "AAPL"
	instance = sv.stockViewer(ticker)
	instance.d2d_pctchange()
	# instance.plot_dpc()
	instance.add_trend()
	instance.plot_trend_piechart()

	print("Candle Recognition")
	candle = cr.candleRecognition(instance.get_df())

if __name__ =="__main__":
	main()