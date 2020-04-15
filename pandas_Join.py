import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

print(left)
print(right)
print(" ")
print(pd.merge(left, right, on='key'))
print(" ")

#two ways to Join

left1 = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right1 = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

print(left1)
print(right1)
print(" ")
print(pd.merge(left, right, on='key'))