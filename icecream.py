import csv
import numpy as np

def getDataSource(data_path):
    temp= []
    sale = []

    
    with open (data_path)as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            temp.append(float(row["Temperature"]))
            sale.append(float(row["Ice-cream Sales"]))

    return{"x":temp,"y":sale}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between temprature and sale is",correlation[0,1])

def main():
    data_path = "icecream.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

main()


