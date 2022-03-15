import csv 
import pandas as pd
import plotly.express as px

with open ('123.csv') as f:
    read = csv.reader(f)
    file_data = list(read)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(int(n_num))

n = len(new_data)
total = 0 
for x in new_data:
    total += x
mean = total/n

print("Mean is:"+ str(round(mean)))

a = pd.read_csv("123.csv")
fig = px.scatter(a, x = "Roll", y = "Marks")
fig.update_layout(shapes = [dict(type = "line", y0 = mean, y1 = mean, x0 = 0, x1 = n)])
fig.show()

