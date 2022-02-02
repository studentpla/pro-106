import csv
import numpy as np

def getDataSource(data_path):
    size = []
    hours = []
    with open (data_path)as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            size.append(float(row["Size of TV"]))
            hours.append(float(row["Average time"]))

    return{"x":size,"y":hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of tv and watching hours is",correlation[0,1])

def main():
    data_path = "tv.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

main()