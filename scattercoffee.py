import csv
import plotly.express as px

with open ("coffee.csv")as f:
    csv_reader = csv.DictReader(f)
    fig = px.scatter(csv_reader, x = "Coffee in ml",y = "sleep in hours") 
    fig.show()