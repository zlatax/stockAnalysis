import matplotlib.pyplot as plt
import pandas_datareader.data as web
import numpy as np


class stockViewer():
  def __init__(self,ticker):
    self.ticker = ticker
    self.df = web.DataReader(self.ticker,
                    start="20200101",
                    end="20201208",
                    data_source="yahoo")

  def d2d_pctchange(self, inplace=True):
    self.df["Day_Pct_Change"] = self.df['Adj Close'].pct_change()*100
    
    self.df.dropna(axis=0,inplace=inplace)
    print(self.df.head())

  def plot_dpc(self):
    self.df['Day_Pct_Change'].plot(title=self.ticker,                                            ylabel="Day Percentage Change")
    plt.show()

  def bull_or_bear(self, x):
    if x > -0.5 and x <= 0.5:
      return 'Slight or No change'
    elif x > 0.5 and x <= 1:
      return 'Slight Positive'
    elif x > -1 and x <= -0.5:
      return 'Slight Negative'
    elif x > 1 and x <= 3:
      return 'Positive'
    elif x > -3 and x <= -1:
      return 'Negative'
    elif x > 3 and x <= 7:
      return 'Among top gainers'
    elif x > -7 and x <= -3:
      return 'Among top losers'
    elif x > 7:
      return 'Bull run'
    elif x <= -7:
      return 'Bear drop'

  def add_trend(self):
    self.df['Trend'] = np.zeros(self.df['Day_Pct_Change'].count())
    print(self.df.tail())
    self.df['Trend'] = self.df['Day_Pct_Change'].apply(lambda x: self.bull_or_bear(x))
    print(self.df.head())

  def plot_trend_piechart(self):
    pie_data = self.df.groupby('Trend')
    pie_label = sorted([i for i in self.df.loc[:,'Trend'].unique()])
    plt.pie(pie_data['Trend'].count(), labels = pie_label,autopct='%1.1f%%',radius=2)
    plt.show()

  def get_df(self):
    return self.df

def main():
  ticker = "AAPL"
  instance = stockViewer(ticker)
  instance.d2d_pctchange()
  # instance.plot_dpc()
  instance.add_trend()
  instance.plot_trend_piechart()
  

if __name__ == "__main__":
  main()
