import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []

    
    with open (data_path)as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return{"x":coffee,"y":sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between coffee and sleeping hours is",correlation[0,1])

def main():
    data_path = "coffee.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

main()


