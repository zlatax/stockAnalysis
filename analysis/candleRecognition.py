# candleRecognition.py
# This program contains methods and functions which takes in and analyses candle chart patterns.

import talib
from analysis import stockViewer as sv

candle_names = talib.get_function_groups()['Pattern Recognition']

print("Candle Names")
print(candle_names)

class candleRecognition():
	def __init__(self,data=None):
		if data == None:
			self.data = sv.stockViewer().df
		else:
			self.data = data

	def get_pattern_names(self):
		return talib.get_function_groups()['Pattern Recognition']

	


