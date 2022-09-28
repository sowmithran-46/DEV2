# -*- coding: utf-8 -*-
"""dev assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v2Am8GqrmFsW1DondgLr64hcYjDdr68P
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/content/International_Report_Departures.csv')
df1=df.head(50)
df1

df1.info()

import seaborn as sns
sns.jointplot(df1['Year'],df1['Month'])

sns.distplot(df1['Year'])

sns.barplot(df1['Year'],df1['Month'])

sns.pairplot(df1[['Year','Month']])

sns.stripplot(df1['Year'],df1['Month'])