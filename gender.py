import pandas as pd
import matplotlib.pyplot as plt

nutri = pd.read_csv('nutri.csv')
males = nutri[nutri.gender == 'male']
females = nutri[nutri.gender == 'female']
plt.boxplot([males.coffee, females.coffee], notch=True, widths=(0.4, 0.4))
plt.xlabel('gender')
plt.ylabel('coffee')
plt.xticks([1,2], ['male', 'female'])
plt.show()