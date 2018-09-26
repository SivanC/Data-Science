#Make sure to 'pip install plotly' on your machine (or however macs do it)
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

#Instantiating minutes and frequencies + axes
xAxis = np.arange(0,211,30)
yAxis = []
hwTimes = [30,10,20,120,210,120,120,30,45,180,0,120,90,0,0,120]

#Forming the y axis by looking through at every interval on the x and seeing how many times are below the threshold
for i in xAxis:
    freqCount = 0
    for j in hwTimes:
        if j <= i:
            freqCount += 1
    yAxis.append(freqCount)

#Plotting the data! A nice graph should appear in your browser.
plot([go.Scatter(x = xAxis, y = yAxis, mode='markers')], filename = 'test_graph.html')