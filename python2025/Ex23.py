import matplotlib.pyplot as plt
import numpy as np

fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']

sales = [400, 350, 300, 450]

plt.bar(fruits, sales)
plt.title('fruit sales')
plt.xlabel('fruits')
plt.ylabel('sales')
plt.show()