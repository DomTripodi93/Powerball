import pandas as pd
import numpy as np
import csv

def get_counts(all_df, df, pos):
    df_in = all_df.iloc[pos,[4,5,6,7,8]]
    df = df.append(df_in)

    num1 = np.array(df.num1)
    num2 = np.array(df.num2)
    num3 = np.array(df.num3)
    num4 = np.array(df.num4)
    num5 = np.array(df.num5)

    all_num = np.append(num1, num2)
    all_num = np.append(all_num, num3)
    all_num = np.append(all_num, num4)
    all_num = np.append(all_num, num5)

    unique, counts = np.unique(all_num, return_counts=True)
    myset = dict(zip(unique, counts))

    return df, myset


def get_base_counts(df):
    num1 = np.array(df.num1)
    num2 = np.array(df.num2)
    num3 = np.array(df.num3)
    num4 = np.array(df.num4)
    num5 = np.array(df.num5)

    all_num = np.append(num1, num2)
    all_num = np.append(all_num, num3)
    all_num = np.append(all_num, num4)
    all_num = np.append(all_num, num5)

    unique, counts = np.unique(all_num, return_counts=True)
    myset = dict(zip(unique, counts))

    return myset