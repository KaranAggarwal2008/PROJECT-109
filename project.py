# We do imports
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random
# reading scores data
df = pd.read_csv("projectData.csv")
data = df["reading score"].tolist()
# Calculating the mean and the standard deviation
# We calculate mean
mean = sum(data) / len(data)
# We calculate standard deviation
std_deviation = statistics.stdev(data)
# We find median
median = statistics.median(data)
# we find mode
mode = statistics.mode(data)
# Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
# We calculate end and start points of standard deviation
first_std_deviation_start, first_std_deviation_end = mean - \
    std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean - \
    (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - \
    (3*std_deviation), mean+(3*std_deviation)
fourth_std_deviation_start, fourth_std_deviation_end = mean - \
    (4*std_deviation), mean+(4*std_deviation)
# Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
trace1=go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN", marker=dict(color='#000000'))
trace2=go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#FF0000'))
trace3=go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#FF0000'))
trace4=go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#00FF00'))
trace5=go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#00FF00'))
trace6=go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#0000FF'))
trace7=go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#0000FF'))
trace8=go.Scatter(x=[fourth_std_deviation_start, fourth_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#FF00FF'))
trace9=go.Scatter(x=[fourth_std_deviation_end, fourth_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1", marker=dict(color='#FF00FF'))
fig.add_traces([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9])
fig.show()
# Printing the findings
list_of_data_within_1_std_deviation = [
    result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [
    result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [
    result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
list_of_data_within_4_std_deviation = [
    result for result in data if result > fourth_std_deviation_start and result < fourth_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(
    len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(
    len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(
    len(list_of_data_within_3_std_deviation)*100.0/len(data)))
print("{}% of data lies within 4 standard deviations".format(
    len(list_of_data_within_4_std_deviation)*100.0/len(data)))
