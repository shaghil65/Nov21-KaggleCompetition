# -*- coding: utf-8 -*-
"""AI_ASSIGNMENT_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uoWLs_O6ODQrLDDOm79tdGDD_wN5SH3l

Accessing Google Drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""
Importing pandas library and getting the whole table by mentioning its path on drive."""

import pandas as pd
h=pd.read_csv('/content/drive/MyDrive/test.csv')
h.head()

"""
Importing numpy and random libraries to get random values."""

import numpy as np
import random

df = pd.read_csv(r'/content/drive/MyDrive/test.csv')

df['RN'] = np.random.uniform(0,1, df.shape[0])
print(df)

"""Applying Condition on RN(Random Number Column) to get the target value"""

df['target'] = [1 if x >= 0.5 else 0 for x in df['RN']]
print(df)

"""Returning a new list by copy function to get the desired column"""

ndf = df[['id','target']].copy()
print(ndf)

"""Finally exporting it to .csv file."""

ndf.to_csv('sample.csv',index=False)