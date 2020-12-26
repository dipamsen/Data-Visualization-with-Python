import csv
import pandas as ps
import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly

df = ps.read_csv("./data/temp.csv")
temperatures = df["temp"].to_list()


def randomData(counter):
    dataset = []
    for i in range(0, counter):
        index = random.randint(0, len(temperatures))
        # dataset.append(temperatures[index])
    mean = statistics.mean(dataset)
    return mean


def plotMean(data):
    sampelmean = statistics.mean(data)
    fig = ff.create_distplot([data], ["Temperature"], show_hist=False)
    fig.add_trace(go.Scatter(
        x=[sampelmean, sampelmean], y=[0, 1], mode="lines"))
    fig.show()


def main():
    meanlist = []
    for i in range(0, 1000):
        mean = randomData(100)
        meanlist.append(mean)
    print("Normal Data")

    plotMean(meanlist)


main()
mean = statistics.mean(temperatures)
print("Mean is ", mean)
# fig = ff.create_distplot([temperatures], ["Temperature"], show_hist=False)

# fig.show()

stdev = statistics.stdev(temperatures)
print("Standard Deviation: ", stdev)

# sample = []
# for i in range(0, 1000):
#     index = random.randint(0, len(temperatures))
#     sample.append(temperatures[index])
# sampleInfo = {
#     "mean": statistics.mean(sample),
#     "stdev": statistics.stdev(sample)
# }
# print("Sample Info")
# print("Mean: ", sampleInfo["mean"])
# print("Standard Deviation: ", sampleInfo["stdev"])
