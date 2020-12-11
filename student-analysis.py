import csv
import plotly_express as px
import pandas as ps

fp = "./data/student-analysis.csv"
df = ps.read_csv(fp)
print(df.groupby("student_id").mean())
px.scatter(df, x="student_id", y="level",
           color="attempt").show()
