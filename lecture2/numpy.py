# -*- coding: utf-8 -*-
"""intro.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gUR2gv0vUG6dQUVvknoz8bLP_PGlPCMA
"""

import numpy as np

array = np.array([1,2,3])
print(array)

array2= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array2.shape)

reshaped = array2.reshape(3,5)
print(reshaped)

#gives row and column
print(reshaped.shape)

#gives dimension
print(reshaped.ndim)

#gives type name
print(reshaped.dtype.name)

#gives size
print(reshaped.size)

#gives dimension
print(reshaped.ndim)

#gives type in python
print(type(reshaped))

array4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array4)
print(array4.shape)

zeros = np.zeros((3,5))
print(zeros)

ones = np.ones((3,5))
ones[0,0] = 5
print(ones)

emptyArray = np.empty((3,3))
print(emptyArray)

#from 5 to 40 by increasing 5 each time
np.arange(5,40,5)

#between 0 and 10, it gives 20 values
np.linspace(0,10,20)

array5 = np.array([1,2,3])
array6 = np.array([4,5,6])
print(array5+array6)
print(array5-array6)
print(array5**2)

array7 = np.array([1,2,3])
array8 = array7
array9 = array8

array9[0] = 90
print(array7,array8,array9)

array10 = array9.copy()
print(array10)
array10[0]=101
print(array7,array8,array9,array10)

array11 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array11)
print(array11[1,1])
print(array11[:,2])
print(array11[0,:])
print(array11[1,1:])

b=np.array([[1,2,3,4,5,6,7],[8,9,11,22,33,44,55]])
b

#all rows first column
print(b[:,1])

#all columns first row
print(b[1,:])

#starts from beginning
print(b[-1,:])

#transform array to one dimentional version
b=np.array([[1,2],[3,4]])
b.ravel()

#transpose
b.T
print(b)