import pandas as ps
import plotly.figure_factory as ff

df = ps.read_csv("./data/mobilesales.csv")
fig = ff.create_distplot([df["Rating"]],
                         ["Rating"])
fig.show()
