# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:56:54 2020

@author: Dell
"""


import pandas as pd

df=pd.read_csv("F:/IIT/Github/TensorFlow-Pokemon-Course/pokemon.csv")

df.columns

df = df[['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed','Color','Egg_Group_1','Height_m','Weight_kg','Body_Style']]

df.columns

df['isLegendary'] = df['isLegendary'].astype(int)
def dummy_creation(df, dummy_categories):
    for i in dummy_categories:
        df_dummy = pd.get_dummies(df[i])
        df = pd.concat([df,df_dummy],axis=1)
        df = df.drop(i, axis=1)
    return(df)
df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1', 'Type_2'])
