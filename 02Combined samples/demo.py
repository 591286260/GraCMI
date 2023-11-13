import csv
import numpy as np
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        SaveList.append(row)
    return
def storFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        # writer = csv.writer(csvfile, )
    return
data1 = []
ReadMyCsv(data1, "../../dataset/755/interaction.csv")
print(len(data1))
data2 = []
ReadMyCsv(data2, "../../01Negative sample generation/NegativeSample.csv")
print(len(data2))
data_final = []
data_final = np.vstack((data1,data2))
print(data_final.shape)
print(data_final)
storFile(data_final, 'Positive and negative samples.csv')