# Visualizing COVID Data
import csv
import pandas as ps
import plotly_express as px

df = ps.read_csv("./data/covid-data.csv")

fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()

# fig = px.bar(df, x="country", y="cases")
# fig.show()
