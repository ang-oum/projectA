________________________________________________
                    input
________________________________________________
myex   = [ex1, ex2]                              Binance Kraken 
mytick = [tick1, tick2]                          BTC/USD  ETH/USD


________________________________________________
                    fetch    2X2 Matrix
________________________________________________
ex1.tick1.close ex1.tick2.close                  BTCUSD    ETHUSD
ex2.tick1.close ex2.tick2.close         Binance  26514.43  1625.28
                                        Kraken   26513.9   1625.28

('binance', 'BTC/USDT', 26514.43)
('binance', 'ETH/USDT', 1625.28)
('kraken', 'BTC/USDT', 26513.9)
('kraken', 'ETH/USDT', 1625.28)
________________________________________________
                    Store
________________________________________________

binance.btc = ('binance', 'BTC/USDT', 26514.43)
binance.eth = ('binance', 'ETH/USDT', 1625.28)
kraken.btc =  ('kraken', 'BTC/USDT', 26513.9)
kraken.eth =  ('kraken', 'ETH/USDT', 1625.28)


'''
[
 ['binance.BTC/USDT', ['binance', 'BTC/USDT', 26503.99]],
 ['binance.ETH/USDT', ['binance', 'ETH/USDT', 1626.28]], 
 ['kraken.BTC/USDT', ['kraken', 'BTC/USDT', 26502.2]],
 ['kraken.ETH/USDT', ['kraken', 'ETH/USDT', 1625.85]]
]
'''

________________________________________________
                    Extract
________________________________________________
mydata[0] = ['binance.BTC/USDT', ['binance', 'BTC/USDT', 26503.99]]
mydata[1] = ['binance.ETH/USDT', ['binance', 'ETH/USDT', 1626.28]]
mydata[2] = ['kraken.BTC/USDT', ['kraken', 'BTC/USDT', 26502.2]]
mydata[3] = ['kraken.ETH/USDT', ['kraken', 'ETH/USDT', 1625.85]]

mydata[0][0] = binance.BTC/USDT
mydata[1][0] = binance.ETH/USDT
mydata[2][0] = kraken.BTC/USDT
mydata[3][0] = kraken.ETH/USDT

mydata[0][1] = ['binance', 'BTC/USDT', 26503.99]
mydata[1][1] = ['binance', 'ETH/USDT', 1626.28]
mydata[2][1] = ['kraken', 'BTC/USDT', 26502.2]
mydata[3][1] = ['kraken', 'ETH/USDT', 1625.85]

mydata[0][1][0] = binance
mydata[1][1][0] = binance
mydata[2][1][0] = kraken
mydata[3][1][0] = kraken

mydata[0][1][1] = BTC/USDT
mydata[1][1][1] = ETH/USDT
mydata[2][1][1] = BTC/USDT
mydata[3][1][1] = ETH/USDT

mydata[0][1][2] =
mydata[1][1][2] = 
mydata[2][1][2] = 
mydata[3][1][2] = 
________________________________________________
                    calculations
________________________________________________

delta = close - close 

________________________________________________
                     output
________________________________________________

0.  delta 

1. max(delta) 

2. min(delta)



datastructure sketch estimate
= {
    "myex"       :   [binance, kraken, bybit,okex] ,
    "mytick"     :   [BTCUSD, ETHUSD, FTMUSD, MATICUSD] ,

    "price"      :   [ex, tick, close, isMax(), isMin()] ,

    "min_close"  :   [ex, tick, close]
    "max_close"  :   [ex, tick, close]

    "expair"     :   [value, ex1, ex2, invexpairvalue] ,
    "delta"      :   [expair, tick, close1, close2, isMin(), isMax()] ,

    "max_delta"  :   [expair, tick, posdelta],
    "min_delta"  :   [invexpair, tick, negdelta],

    ( 
        if invexpair(min_delta) = expair(max_delta):
                print("optimarb found")
    )

    "min_optimarb"   :   [expair, min_deltatick, min_deltatickprice, min_delta],
    "max_optimarb"   :   [invexpair, max_deltatick, max_deltatickprice, max_delta],

    "execution_summary" : [steps, profitmargin],
    "steps"             : [step1, step2, step3, step4, step5],



}










[ta]
[tradingview-ta]
[pandas-datareader]
(pytz, urllib3, tzdata, six, numpy, lxml, idna, charset-normalizer, certifi, requests, python-dateutil, pandas, pandas-datareader )
[yfinance]
(webencodings, multitasking, appdirs, soupsieve, html5lib, frozendict, beautifulsoup4, yfinance)
[backtesting]
(xyzservices, tornado, PyYAML, pillow, packaging, MarkupSafe, contourpy, Jinja2, bokeh, backtesting)
[ccxt]
(setuptools, pycparser, multidict, frozenlist, attrs, async-timeout, yarl, cffi, aiosignal, pycares, cryptography, aiohttp, aiodns, ccxt)
[lightweight-charts]
(proxy-tools, bottle, typing-extensions, clr-loader, pythonnet, pywebview, lightweight-charts)
[binance-futures-connector]
(websocket-client, pycryptodome, binance-futures-connector)