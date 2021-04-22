import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("./data/medium_data.csv")
likes = df['reading_time']
likes = likes[likes.notna()]
pop_mean = likes.mean()


def sample(num):
  sampled_data = likes.sample(n=num)
  return sampled_data.mean()


def setup():
  means = []
  for i in range(1, 100):
    s = sample(i)
    means.append(s)
  meanlist = means

  sample_mean = statistics.mean(meanlist)
  print("Population Mean", pop_mean)
  print("Sampled Mean", sample_mean)
  show_fig(meanlist)


def show_fig(meanlist):
  ff.create_distplot([meanlist], ["Reading Time"], show_hist=False).show()


setup()
