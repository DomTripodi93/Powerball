import pandas as pd
import numpy as np
import csv
from get_counts import get_counts as gc
from get_counts import get_base_counts as gbc
from check_last import check_last as cl

all_df = pd.read_csv('powerball.csv')
base_df = pd.read_csv('2010.csv')
base_counts = gbc(pd.read_csv('2010.csv'))
print(base_counts)
df_start = pd.DataFrame()
df_start = all_df.iloc[0,[4,5,6,7,8]]
length = len(all_df.index)
print(len(base_df.index))
comparisons = pd.DataFrame()

csv_file = "occurrences.csv"
pb_file = "pbOccurrences.csv"
columns = ["number", "occurrences"]

for location in range(0, length):
    base_df, base_counts = gc(all_df, base_df, location)
    comparisons = comparisons.append(cl(all_df, base_counts, location))

comparisons.to_csv(r'comparisons.csv', index=False)