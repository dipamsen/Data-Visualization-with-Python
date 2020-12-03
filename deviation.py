import csv
import pandas as ps
import plotly_express as px


with open("data/marks.csv", newline="") as file:
    rdr = csv.reader(file)
    marks = list(rdr)
    marks.pop(0)
    total = 0
    for name, score in marks:
        total += float(score)
    mean = total/len(marks)
    print("Total is " + str(total))
    print("Mean is " + str(mean))

    df = ps.read_csv("data/marks.csv")
    fig = px.scatter(df, x="Student Number", y="Marks")

    fig.update_layout(
        shapes=[dict(type="line", x0=0, x1=len(df), y0=mean, y1=mean)])

    fig.show()
