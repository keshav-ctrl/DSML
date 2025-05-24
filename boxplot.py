import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nutri = pd.read_csv('nutri.csv')
width = 0.15 
plt.boxplot(nutri['age'], widths=width, vert=False)
# widths parameter determines the width of he boxplt, vert= False plots the boxplot at horizontally
plt.xlabel('age')
plt.show()