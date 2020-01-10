import numpy as np
import pandas as pd
'''
np.max() = max value
np.argmax() = position of max value
np.dtype = element type

np.mean() = mean value
np.std() = standered deviation
np.sum() = finds sum

vectorized operations 
add: +
subract: -
multiply: *
divide: /
Exponentiate: **

Logic: (Need bool)
and: &
or: |
not: ~

comparison:
greater: >
greater or equal: >=
less: <
less or equal: <=
equal: ==
not equal: !=

a = np.array([1,2,3,4,5])
b = np.array([False,False,True,True,True])
a[b] == 3,4,5
a[a>2] == 3,4,5


a = np.array([1,2,3,4])
a = b
a += np.array([1,1,1,1]) #this would add the array to a and b
a = a + np.array([1,1,1,1]) #this would add the array to only a 


Pandas series (still can do same things as numpy i.e. (s.meanm s.max, etc.))

s.describe() = #gives count, mean, SD, etc. 
has index
s = pd.Series(data=[1, None, 4, 3, 4],
                        index=['A', 'B', 'C', 'D', 'E'])

s.loc('index') #looks up data by index

#need to add series with same indexes
    #.dopna gives back only numbrs with same index

s.apply(function) #applies a function to each data point in the series



for numpy arrays
use axis = 0 to calculate data for a colomn and axis = 1 for row. Ex(mean(axis = 1) calculates the mean for the row)


for dataframs (good for CSV files)
use .loc to acess rows by indexes and .iloc to get rows by possition to get position you can use .loc or .iloc but give row and position
can use .value to get a numpy array of just the values

df.applymap applies a function to the specified row or column in the data frame
