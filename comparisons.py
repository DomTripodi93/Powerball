import pandas as pd
import numpy as np
import csv
from get_counts import get_counts as gc
from get_counts import get_base_counts as gbc
from check_last import check_last as cl
from check_last import check_percent as cp

print("Please wait while we analyze the results")

all_df = pd.read_csv('powerball.csv')
base_df = pd.read_csv('2010.csv')
base_counts = gbc(pd.read_csv('2010.csv'))
df_start = pd.DataFrame()
df_start = all_df.iloc[0,[4,5,6,7,8]]
length = len(all_df.index)
comparisons = pd.DataFrame()
percentages = pd.DataFrame()

csv_file = "occurrences.csv"
pb_file = "pbOccurrences.csv"
columns = ["number", "occurrences"]

for location in range(0, length):
    base_df, base_counts = gc(all_df, base_df, location)
    comp_hold = cl(all_df, base_counts, location)
    comparisons = comparisons.append(comp_hold)
    percentages = percentages.append(cp(comp_hold, location))

comparisons.to_csv(r'results/comparisons.csv', index=False)
percentages.to_csv(r'results/percentages.csv', index=False)

print("Complete, CSV Results now available")