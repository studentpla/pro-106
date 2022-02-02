import csv
import numpy as np

def getDataSource(data_path):
    MarksInPercentage = []
    DaysPresent = []

    
    with open (data_path)as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            MarksInPercentage.append(float(row["MarksInPercentage"]))
            DaysPresent.append(float(row["DaysPresent"]))

    return{"x":MarksInPercentage,"y":DaysPresent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between days student are present and their marks is",correlation[0,1])

def setup():
    data_path = "percentage.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
