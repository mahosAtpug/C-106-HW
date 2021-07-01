import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days_present = []

    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks"]))
            days_present.append(float(row["Days Present"]))
        
        print(days_present)

    return {"x":marks , "y":days_present}

def plotFigure(data_path):
    with open (data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df , x="Days Present" , y="Marks")
        fig.show()

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"] , datasource["y"])

    print("Correlation in Present Days vs Marks ->" , correlation[0 , 1])

def setup():
    data_path = "marksvsattendance.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
        