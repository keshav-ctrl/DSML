import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nutri = pd.read_csv('nutri.csv')
x = np.sort(nutri.age)
y = np.linspace(0, 1, len(nutri.age))
plt.xlabel('age')
plt.ylabel('Fn(x)')
plt.step(x,y)
plt.xlim(x.min(), x.max())
plt.show()
