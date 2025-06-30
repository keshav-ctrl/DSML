import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nutri = pd.read_csv('nutri.csv')
sns.countplot(x='situation', hue='gender', data=nutri, hue_order=['male', 'female'],
              palette=['skyblue','pink'], saturation=1, edgecolor = 'black')
plt.legend(loc='upper center')
plt.xlabel('')
plt.ylabel('counts')
plt.show()