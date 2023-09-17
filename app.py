import ccxt
import pandas as pd
from lightweight_charts import Chart

mydata = []
def getprices(exchange, symbol):
  inst = getattr(ccxt, exchange)() #instantiate
  ohlcv = inst.fetchOHLCV(symbol, limit=1)
  closing_price = ohlcv[0][4]
  list = [
    exchange+"."+symbol , [exchange, symbol, closing_price]
  ]
  mydata.append(list)
  return list

myex =  [ 'binance', 'kraken']
mytick = ['BTC/USDT', 'ETH/USDT']
for ex in myex:
  for tick in mytick:
    data = getprices(ex, tick)
    print(data)
print(mydata)







'''
[
 ['binance.BTC/USDT', ['binance', 'BTC/USDT', 26503.99]],
 ['binance.ETH/USDT', ['binance', 'ETH/USDT', 1626.28]], 
 ['kraken.BTC/USDT', ['kraken', 'BTC/USDT', 26502.2]],
 ['kraken.ETH/USDT', ['kraken', 'ETH/USDT', 1625.85]]
]
'''






#getprices('deribit', 'BTC/USDT') #no btc/usdt
#getprices('upbit', 'BTC/USDT')   #fetch not live


































'''
if __name__ == '__main__':
  chart = Chart()

  df = pd.read_csv( 'csv file' )
  chart.set(df)

  chart.show(block=True)
'''



'''
prices = []
fails = []

for ex in ccxt.exchanges:
  try:
    prices.append(getprices(ex, 'BTC/USDT'))
    print('Price fetched from:' +ex )
  except:
    fails.append(ex)
    print('Failed fetch from:' +ex)
'''

