# ------------------------------------------------------ #
# Module & Libraries Import
# ------------------------------------------------------ #
import pandas as pd
from pandas_datareader import data as pdr


# ------------------------------------------------------ #
# Function to get stocks data from Yahoo! Finance
# ------------------------------------------------------ #
def get_stock_data(tick, start_date, end_date=None, r='d'):
    stock_df = pd.DataFrame()
    volume_df = pd.DataFrame()
    tentative = 0
    bucket = []
    while len(tick) != 0 and tentative < 5:
        tick = [j for j in tick if j not in bucket]
        for i in range(len(tick)):
            try:
                temp = pdr.get_data_yahoo(tick[i],
                                          start=start_date,
                                          end=end_date,
                                          interval=r)
                stock_df[tick[i]] = temp['Adj Close']
                volume_df[tick[i]] = temp['Volume']
                bucket.append(tick[i])
            except:
                print('Failed to retrieve {} stock data... retrying'.format(tick[i]))
                continue
        tentative = tentative + 1
    return stock_df.dropna(), bucket, volume_df.dropna()