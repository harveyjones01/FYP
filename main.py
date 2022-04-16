import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
import getCurrentdata
import dataCleaning

days_in_advance = 31

dataCleaning.clean(days_in_advance)

df = pd.read_csv('new.csv')
df = df.dropna()
x_cols = ['Price', 'Open', 'High', 'Low', 'Vol.']
y_cols = ['Class']

y = df[y_cols]
x = df[x_cols]

clf = RandomForestClassifier(random_state=1000).fit(x.values, y.values.ravel())

In = getCurrentdata.get_data()
print('bitcoin is currently a', clf.predict([In])[0], 'investment')