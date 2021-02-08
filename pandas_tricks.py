# using group by nicely 

import pandas as pd


pd.set_option("max_columns", 8)
df = pd.read_csv('http://bit.ly/drinksbycountry')
#df.to_csv('drinksbycountry.csv')


print(df.head())


'''
select continent,
       sum(total_litres_of_pure_alcohol) as total,
       sum(total_litres_of_pure_alcohol) as count
from df
group by continent 
'''

df2 =pd.pivot_table(df, index='continent',
                        values= 'total_litres_of_pure_alcohol',
                        aggfunc={'total_litres_of_pure_alcohol' :
                                 ['sum', 'count']}).reset_index()\
                        .rename({'sum': 'total'},
                                axis='columns')


# using groupby
df.groupby(['continent']).agg({'total_litres_of_pure_alcohol': sum})
  .rename(columns={'total_litres_of_pure_alcohol':'SUM'})



#df2.columns.rename({'total_litres_of_pure_alcohol': 'total'}, inplace=True)
print('#----------------------#')
print(df2)
