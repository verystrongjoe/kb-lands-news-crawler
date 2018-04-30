import  pandas as pd
import csv

# str = 'a,bcd'
# print(str.replace(',', '\,'))


df = pd.read_csv('results.csv',  sep=',\s+', quoting=csv.QUOTE_ALL, encoding='utf-8')
print(df.head(10))

