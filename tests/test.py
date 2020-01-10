import numpy as np
import pandas as pd
a = pd.Series(data=[1,2,4,6,7,4,9])


filename = 'nyc_subway_weather.csv'
subway_df1 = pd.read_csv(filename)
subway_df = subway_df1.corr(method = 'pearson')
print(subway_df)

print('|||||||||||||||||||||||||||||||||||||||||')

print(subway_df.loc['ENTRIESn','EXITSn'])