# Single line graph

import matplotlib.pyplot as plt

# Data for the line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the line graph
plt.plot(x, y)

# Add title and labels
plt.title('Line Graph Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the graph
plt.show()
