import numpy as np
import pandas
#'''
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

s.describe() = 
'''