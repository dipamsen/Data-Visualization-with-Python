import pandas as ps
import statistics
import csv

df = ps.read_csv("./data/heightweight2.csv")
heights = df['Height'].to_list()
hmean = statistics.mean(heights)
hmedian = statistics.median(heights)
hmode = statistics.mode(heights)
hstdev = statistics.stdev(heights)

hfirststart_stdev, hfirstend_stdev = hmean - hstdev, hmean + hstdev
hsecondstart_stdev, hsecondend_stdev = hmean - (2*hstdev), hmean + (2*hstdev)
hthirdstart_stdev, hthirdend_stdev = hmean - (3*hstdev), hmean + (3*hstdev)

hlistDatawithinOneStDev = [
    result for result in heights if result > hfirststart_stdev and result < hfirstend_stdev]
hlistDatawithinTwoStDev = [
    result for result in heights if result > hsecondstart_stdev and result < hsecondend_stdev]
hlistDatawithinThreeStDev = [
    result for result in heights if result > hthirdstart_stdev and result < hthirdend_stdev]

print("Mean: ", hmean)
print("Median: ", hmedian)
print("Mode: ", hmode)
print("Standard Deviation: ", hstdev)
print("{} Percentage of Data lying between first StDev".format(
    len(hlistDatawithinOneStDev)*100/len(heights)))
print("{} Percentage of Data lying between second StDev".format(
    len(hlistDatawithinTwoStDev)*100/len(heights)))
print("{} Percentage of Data lying between third StDev".format(
    len(hlistDatawithinThreeStDev)*100/len(heights)))


weights = df['Weight'].to_list()
wmean = statistics.mean(weights)
wmedian = statistics.median(weights)
wmode = statistics.mode(weights)
wstdev = statistics.stdev(weights)

wfirststart_stdev, wfirstend_stdev = wmean - wstdev, wmean + wstdev
wsecondstart_stdev, wsecondend_stdev = wmean - (2*wstdev), wmean + (2*wstdev)
wthirdstart_stdev, wthirdend_stdev = wmean - (3*wstdev), wmean + (3*wstdev)

wlistDatawithinOneStDev = [
    result for result in weights if result > wfirststart_stdev and result < wfirstend_stdev]
wlistDatawithinTwoStDev = [
    result for result in weights if result > wsecondstart_stdev and result < wsecondend_stdev]
wlistDatawithinThreeStDev = [
    result for result in weights if result > wthirdstart_stdev and result < wthirdend_stdev]

print("Mean: ", wmean)
print("Median: ", wmedian)
print("Mode: ", wmode)
print("Standard Deviation: ", wstdev)
print("{} Percentage of Data lying between first StDev".format(
    len(wlistDatawithinOneStDev)*100/len(weights)))
print("{} Percentage of Data lying between second StDev".format(
    len(wlistDatawithinTwoStDev)*100/len(weights)))
print("{} Percentage of Data lying between third StDev".format(
    len(wlistDatawithinThreeStDev)*100/len(weights)))
