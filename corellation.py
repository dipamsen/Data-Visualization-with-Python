# Corellation

import numpy as np
import csv
import plotly_express as px
import pandas as ps

csvfile = open("./data/marks-days.csv")
data = list(csv.reader(csvfile))
data.pop(0)
marks = []
days = []
for rn, mk, dy in data:
    marks.append(float(mk))
    days.append(int(dy))

print(np.corrcoef(marks, days))
px.scatter(ps.read_csv("./data/marks-days.csv"), x="Marks", y="Days").show()
