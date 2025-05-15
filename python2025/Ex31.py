# Histogram in histogram

import matplotlib.pyplot as plt
#sample data	
data=[60,66,70,74,73,77,66,65,80,88,90,80,81,68,90,70,77,75,80,63,61,70,55,54,65,56,92,89,85,80,81]
data1=[60,66,70,74,73,77,66,65,80,88,90,80,81,68,90,70,77,75,80,63,61,70,55,65,56,98,92,89,85,80,81]
#create histogram	
plt.hist(data, bins=4, color="black", edgecolor="green")
plt.hist(data1, bins=4, color="red", edgecolor="green")
plt.xlabel("division")
plt.ylabel("mark")
plt.title("histogram")
plt.show()