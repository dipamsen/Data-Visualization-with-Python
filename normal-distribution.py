# Normal Distribution

import csv
import plotly.figure_factory as ff
import plotly.express as px
import pandas as ps

df = ps.read_csv('./data/heightweight2.csv')
fig = ff.create_distplot([df["Weight"].to_list()], ["Weight"], show_hist=False)
fig.show()
