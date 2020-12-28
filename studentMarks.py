import pandas as ps
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

data1 = ps.read_csv("./data/mathData1.csv")
data2 = ps.read_csv("./data/mathData2.csv")
data3 = ps.read_csv("./data/mathData3.csv")
mean1 = statistics.mean(data1)
mean2 = statistics.mean(data2)
mean3 = statistics.mean(data3)

fig = ff.create_distplot([])


def randomStudents(count):
    dataset = []
    for i in range(0, count):
        index = random.randint(0, len(data)-1)
        dataset.append(data[index])
    mean = statistics.mean(dataset)

    return mean


meanlist = []
for i in range(0, 1000):
    meanlist.append(randomStudents(100))
mean = statistics.mean(meanlist)
stdev = statistics.stdev(meanlist)
# print("Mean:", mean)
# print("STDEV:", stdev)
fig = ff.create_distplot([meanlist], ["Math Scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean1, mean1], y=[
              0, 0.2], mode="lines", name="Mean1"))
fig.add_trace(go.Scatter(x=[mean2, mean2], y=[
              0, 0.2], mode="lines", name="Mean2"))
fig.add_trace(go.Scatter(x=[mean3, mean3], y=[
              0, 0.2], mode="lines", name="Mean3"))
first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - 2*stdev, mean + 2*stdev
third_stdev_start, third_stdev_end = mean - 3*stdev, mean + 3*stdev
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[
              0, 0.2], mode="lines", name="First StDev Start"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[
              0, 0.2], mode="lines", name="First StDev End"))
# fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[
#               0, 0.2], mode="lines", name="Second StDev Start"))
# fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[
#               0, 0.2], mode="lines", name="Second StDev End"))
# fig.add_trace(go.Scatter(x=[third_stdev_start, third_stdev_start], y=[
#               0, 0.2], mode="lines", name="Third StDev Start"))
# fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[
#               0, 0.2], mode="lines", name="Third StDev End"))
# print("First Standard Deviation Range", first_stdev_start, first_stdev_end)
# print("Second Standard Deviation Range", second_stdev_start, second_stdev_end)
# print("Third Standard Deviation Range", third_stdev_start, third_stdev_end)
# mean = statistics.mean(data)
# stdev = statistics.stdev(data)

fig.show()
