import pandas as pd
import numpy as np
import csv

def check_last(all_df, base_counts, pos):
    df_in = all_df.iloc[pos,[4,5,6,7,8]]
    myDict = {
        'first': [base_counts[df_in["num1"]]],
        'second': [base_counts[df_in["num2"]]],
        'third': [base_counts[df_in["num3"]]],
        'fourth': [base_counts[df_in["num4"]]],
        'fifth': [base_counts[df_in["num5"]]]
    }

    data = pd.DataFrame(data=myDict)

    return data