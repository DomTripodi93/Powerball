import pandas as pd
import numpy as np
import csv

def check_last(all_df, base_counts, pos):
    df_in = all_df.iloc[pos,[4,5,6,7,8]]
    comp_dict = {
        'First': [base_counts[df_in["num1"]]],
        'Second': [base_counts[df_in["num2"]]],
        'Third': [base_counts[df_in["num3"]]],
        'Fourth': [base_counts[df_in["num4"]]],
        'Fifth': [base_counts[df_in["num5"]]],
    }

    comp_data = pd.DataFrame(data=comp_dict)

    return comp_data

def check_percent(comp_df, pos):
    avg = (pos+104)/11

    percent_dict = {
        '1%': [str(round(comp_df['First'][0]/avg*100)) + "%"],
        '2%': [str(round(comp_df['Second'][0]/avg*100)) + "%"],
        '3%': [str(round(comp_df['Third'][0]/avg*100)) + "%"],
        '4%': [str(round(comp_df['Fourth'][0]/avg*100)) + "%"],
        '5%': [str(round(comp_df['Fifth'][0]/avg*100)) + "%"],
    }

    percent_data = pd.DataFrame(data=percent_dict)

    return percent_data