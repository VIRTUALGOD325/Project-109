import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics


df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
sd = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_SD_start, first_SD_end = mean-sd, mean+sd
second_SD_start, second_SD_end = mean-(2*sd), mean+(2*sd)
third_SD_start, third_SD_end = mean-(3*sd), mean+(3*sd)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

fig.add_trace(go.Scatter(x=[first_SD_start, first_SD_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_SD_end, first_SD_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_SD_start, second_SD_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_SD_end, second_SD_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

list_of_data_within_1_SD = [result for result in data if result > first_SD_start and result < first_SD_end]
list_of_data_within_2_SD = [result for result in data if result > second_SD_start and result < second_SD_end]
list_of_data_within_3_SD = [result for result in data if result > third_SD_start and result < third_SD_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(sd))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_SD)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_SD)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_SD)*100.0/len(data)))