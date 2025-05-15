# Histogram using python

import matplotlib.pyplot as plt
# Sample data
data = [12, 15, 13, 12, 18, 19, 21, 21, 22, 25, 25, 25, 30, 31, 35, 40]
# Create histogram
plt.hist(data, bins=3, color='pink', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Show the plot
plt.show()