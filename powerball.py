import pandas as pd
import numpy as np
from scipy import stats
import csv

print("Please wait while we analyse the results")

df = pd.read_csv('powerball.csv')

csv_file = "occurrences.csv"
pb_file = "pbOccurrences.csv"
columns = ["number", "occurrences"]

num1 = np.array(df.num1)
num2 = np.array(df.num2)
num3 = np.array(df.num3)
num4 = np.array(df.num4)
num5 = np.array(df.num5)

all_num = np.append(num1, num2)
all_num = np.append(all_num, num3)
all_num = np.append(all_num, num4)
all_num = np.append(all_num, num5)


pb = np.array(df.pball)

unique, counts = np.unique(all_num, return_counts=True)
myset = dict(zip(unique, counts))

unique2, counts2 = np.unique(pb, return_counts=True)
pbset = dict(zip(unique2, counts2))

with open(csv_file, 'w') as csvfile:
    csvfile.write("%s,%s\n"%(columns[0],columns[1]))
    for key in myset.keys():
        csvfile.write("%s,%s\n"%(key,myset[key]))

with open(pb_file, 'w') as csvfile:
    csvfile.write("%s,%s\n"%(columns[0],columns[1]))
    for key in pbset.keys():
        csvfile.write("%s,%s\n"%(key,pbset[key]))

print("Complete, CSV Results now available")