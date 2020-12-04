
import pandas as ps
import plotly_express as px
import csv
import numpy


def read(path, a, b):
    icecream = []
    colddrink = []
    with open(path) as csvfile:
        rd = csv.DictReader(csvfile)
        for val in rd:
            icecream.append(float(val[a]))
            colddrink.append(float(val[b]))
    return {"x": icecream, "y": colddrink}


def corellation(data):
    corellation = numpy.corrcoef(data["x"], data["y"])
    print(corellation[0, 1])


def main():
    path = "./data/coffee-sleep.csv"
    data = read(path, "Coffee", "Sleep")
    corellation(data)
    px.scatter(ps.read_csv(path), x="Coffee", y="Sleep").show()


main()
