# Box Plot

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
d = np.random.normal(100, 20, 200)

fig = plt.figure(figsize =(10, 7))

plt.boxplot(d)
plt.show()


