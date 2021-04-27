import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv("./data/medium_data.csv")
rt = df['reading_time']
rt = rt[rt.notna()]
pop_mean = rt.mean()


def get_sample_mean(data):
  return data.sample(n=30).mean()


def plot_graph(meanlist):
  fig = ff.create_distplot([meanlist], ["Reading Time"], show_hist=False)
  return fig


def setup():
  meanlist = []
  for i in range(100):
    meanlist.append(get_sample_mean(rt))

  mean = statistics.mean(meanlist)
  std_deviation = statistics.stdev(meanlist)

  # findig the standard deviation starting and ending values
  first_std_deviation_start, first_std_deviation_end = mean - \
      std_deviation, mean + std_deviation
  second_std_deviation_start, second_std_deviation_end = \
      mean - (2 * std_deviation), mean + (2 * std_deviation)
  third_std_deviation_start, third_std_deviation_end = mean - \
      (3 * std_deviation), mean + (3 + std_deviation)
  print("std1", first_std_deviation_start, first_std_deviation_end)
  print("std2", second_std_deviation_start, second_std_deviation_end)
  print("std3", third_std_deviation_start, third_std_deviation_end)

  fig = plot_graph(meanlist)

  fig.add_trace(go.Scatter(x=[mean, mean], y=[
                0, 0.71], mode="lines", name="MEAN"))
  fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[
                0, 0.71], mode="lines", name="First Stdev Start"))
  fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[
                0, 0.71], mode="lines", name="First Stdev End"))
  fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[
                0, 0.71], mode="lines", name="Second Stdev Start"))
  fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[
                0, 0.71], mode="lines", name="Second Stdev End"))
  fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[
      0, 0.71], mode="lines", name="Third Stdev Start"))
  fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[
                0, 0.71], mode="lines", name="Third Stdev End"))
  fig.show()


setup()
