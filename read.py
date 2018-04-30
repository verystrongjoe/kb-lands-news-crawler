import pandas as pd

df = pd.read_csv('results_bk.csv', encoding='utf-8', header=None, error_bad_lines=False)

print(df.head(1))