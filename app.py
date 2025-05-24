import pandas as pd

xls = 'http://www.biostatisticien.eu/springeR/nutrition_elderly.xls'
nutri = pd. read_excel (xls)
# to fit display
# pd. set_option ('display.max_columns', 8)
# print(nutri.head ())
# to view the general info of data 
# print(nutri.info())

dict = {1:'male', 2:'female'} #dictionary specifies replacement
nutri['gender']=nutri['gender'].replace(dict).astype('category')
dict_2= {1:'single', 2:'living with spouse', 3:'living with family', 4:'living with someone else'}
nutri['situation']=nutri['situation'].replace(dict_2).astype('category')
dict_3={0:'never', 1:'less than one a week', 2:'once a week',3:'2-3 times a week', 4:'4-6 times a week',
        5:'everyday' }
nutri['meat']=nutri['meat'].replace(dict_3).astype('category')
nutri['fish']=nutri['fish'].replace(dict_3).astype('category')
nutri['raw_fruit']=nutri['raw_fruit'].replace(dict_3).astype('category')
nutri['cooked_fruit_veg']=nutri['cooked_fruit_veg'].replace(dict_3).astype('category')
nutri['chocol']=nutri['chocol'].replace(dict_3).astype('category')
dict_4 = {1:'butter', 2:'margarine', 3:'peanut oil', 4:'sunflower oil', 5:'olive oil',
          6:'mix of vegetables oil', 7:'colza oil', 8:'duck or goose fat'}
nutri['fat']=nutri['fat'].replace(dict_4).astype('category')
print(nutri.head())
nutri.to_csv('nutri.csv', index=False)