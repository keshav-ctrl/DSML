import pandas as pd
data = pd.read_csv('nutri.csv')
# print(data['fat'].describe()) #for a single column describe
# print(data[['gender','situation', 'fat', 'meat','fish', 'chocol']].describe()) #for nultible columns describe 
# print(data['fat'].value_counts())
# con= pd.crosstab(data.gender, data.situation, margins= True)
# print(con)
# print(data['height'].mean())
# quantile = data['height'].quantile(q=[0.25,0.50,0.75])
# print(quantile)

# print(data['height'].max()- data['height'].min())

# var = round(data['height'].var(), 2) # rounded in two decimal places.
# std = round(data['height'].std(), 2)
# print("Variance is:", var)
# print("Standard deviation is:", std)

print(data['height'].describe())