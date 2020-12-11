#readme.md

# stockAnalysis

stockAnalysis is a Python Application for analysing stock tickers with matplotlib and ta-lib.
Additional candlestick pattern recognition is implemented to provide insight for potential trading bot.

## Installation

//SAMPLE
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install stockAnalysis.

```bash
pip install foobar
```

## Usage

```python
import stockAnalysis.analysis as sa 

instance = sa.stockViewer("IBM") # a stockViewer object with functions to analyse a certain ticker.
instance = sa.candleRecognition() # candleRecognition object with tools to analyse market data ascandlestick patterns.
¥
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
