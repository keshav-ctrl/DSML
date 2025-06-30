import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nutri = pd.read_csv('nutri.csv')
weights = np.ones_like(nutri.age)/ nutri.age.count()
plt.hist(nutri.age, bins = 10, weights = weights, 
         facecolor = 'cyan', edgecolor = 'black', linewidth = 1)
plt.xlabel('age')
plt.ylabel('Proportion of Total')
plt.show()

