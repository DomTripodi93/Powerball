import pandas as pd
import numpy as np

print("Please wait while we analyze the results")

df = pd.read_csv('results/occurrences.csv')
percent_dict = {}
percent_by_number_file = "results/percent_by_number.csv"
columns = ["number", "percentage"]

for number in range(0,69):
    avg = 106/11
    percent_dict[number+1] = str(round(df["occurrences"][number]/avg*100)) + "%"

with open(percent_by_number_file, 'w') as csvfile:
    csvfile.write("%s,%s\n"%(columns[0],columns[1]))
    for key in percent_dict.keys():
        csvfile.write("%s,%s\n"%(key,percent_dict[key]))

print("Complete, CSV Results now available")