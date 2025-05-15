
# Displaying marks of student in histogran using python

import matplotlib.pyplot as plt
import random

# Generate 32 random marks between 0 and 100
marks = [random.randint(0, 100) for _ in range(32)]

# Categorize results
first_class = [mark for mark in marks if mark >= 60]
second_class = [mark for mark in marks if 50 <= mark < 60]
SP = [mark for mark in marks if mark < 50]

# Prepare histogram data
categories = ['1st Class', '2nd Class', 'SP']
counts = [len(first_class), len(second_class), len(SP)]

# Plot the histogram
plt.bar(categories, counts, color=['pink', 'purple', 'blue'])
plt.title('Results Distribution (32 Units)')
plt.xlabel('Result Category')
plt.ylabel('Number of Units')
plt.grid(axis='y')
plt.show()