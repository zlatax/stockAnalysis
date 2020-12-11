# candleRecognition.py
# This program contains methods and functions which takes in and analyses candle chart patterns.

import talib
import analysis.stockViewer as sv

candle_names = talib.get_function_groups()['Pattern Recognition']


class candleRecognition():
	def __init__(self,data):
		if data.empty:
			self.data = sv.stockViewer().df
		else:
			self.data = data
		self.pattern_columns()

	def get_pattern_names(self):
		return talib.get_function_groups()['Pattern Recognition']

	def pattern_columns(self):
		#extract OHLC
		op = self.data['Open']
		hi = self.data['High']
		lo = self.data['Low']
		cl = self.data['Close']

		for candle in self.get_pattern_names():
			self.data = getattr(talib, candle)(op,hi,lo,cl)

		print(self.data.head(10))

