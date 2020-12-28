import pandas as ps

import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

marks = ps.read_csv("./data/studentMarks.csv")['Math_score'].to_list()
meanTotal = statistics.mean(marks)
stdevTotal = statistics.stdev(marks)
print("Mean:", meanTotal)
print("STDEV:", stdevTotal)


def randomStudents(count):
    dataset = []
    for i in range(0, count):
        index = random.randint(0, len(marks)-1)
        dataset.append(marks[index])
    mean = statistics.mean(dataset)

    return mean


meanlist = []
for i in range(0, 1000):
    meanlist.append(randomStudents(100))
mean = statistics.mean(meanlist)
stdev = statistics.stdev(meanlist)

fig = ff.create_distplot([meanlist], ["Mean list"], show_hist=False)
fig.add_trace(go.Scatter(x=[meanTotal, meanTotal], y=[
              0, 0.2], name="Total Mean", mode='lines'))

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - 2*stdev, mean + 2*stdev
third_stdev_start, third_stdev_end = mean - 3*stdev, mean + 3*stdev

data1 = ps.read_csv("./data/mathData1.csv")['Math_score'].to_list()
mean1 = statistics.mean(data1)
print("Mean of Data 1", mean1)
data2 = ps.read_csv("./data/mathData2.csv")['Math_score'].to_list()
mean2 = statistics.mean(data2)
print("Mean of Data 2", mean2)
data3 = ps.read_csv("./data/mathData3.csv")['Math_score'].to_list()
mean3 = statistics.mean(data3)
print("Mean of Data 3", mean3)

fig.add_trace(go.Scatter(x=[mean3, mean3], y=[
              0, 0.2], name="Mean of Sample Data", mode='lines'))
# fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[
# 0, 0.2], mode="lines", name="First StDev End"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[
              0, 0.2], mode="lines", name="Second StDev End"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[
              0, 0.2], mode="lines", name="Second StDev End"))

zScore1 = (mean1 - mean) / stdev
zScore2 = (mean2 - mean) / stdev
zScore3 = (mean3 - mean) / stdev
print("z-scores: ", zScore1, zScore2, zScore3)


fig.show()
