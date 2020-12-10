import pandas as ps
import plotly.graph_objects as go
import csv


df = ps.read_csv("./data/student-analysis.csv")

student = df.loc[df['student_id'] == 'TRL_987']
print(student.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(x=student.groupby("level")[
    "attempt"].mean(), y=["Level 1", "Level 2", "Level 3", "Level 4"], orientation='h'))
fig.show()
