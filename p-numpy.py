import numpy as np

"CREATING ARRAYS"

# Create a list and convert it to a numpy array
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

# Or just pass in a list directly
y = np.array([4, 5, 6])
print(y)

# Pass in a list of lists to create a "multidimensional array".
m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

# Use the shape method to find the dimensions of the array. (rows, columns)
print(m.shape)

# arange returns evenly spaced values within a given interval.
# start at 0 count up by 2, stop before 30
n = np.arange(0, 30, 2)
print(n)

# reshape returns an array with the same data with a new shape.
# reshape array to be 3x5
n = n.reshape(3, 5)
print(n)

# linspace returns evenly spaced numbers over a specified interval.
# return 9 evenly spaced values from 0 to 4
o = np.linspace(0, 4, 9)
print(o)

# resize changes the shape and size of array in-place.
o.resize(3, 3)
print(o)

# ones returns a new array of given shape and type, filled with ones.
print(np.ones((3, 2)))

# zeros returns a new array of given shape and type, filled with zeros.
print(np.zeros((2, 3)))

# eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
print(np.eye(3))

# diag extracts a diagonal or constructs a diagonal array.
y = np.array([2, 4, 6])
print(np.diag(y))

# Create an array using repeating list (or see np.tile)
print(np.array([1, 2, 3] * 3))

# Repeat elements of an array using repeat.
print(np.repeat([1, 2, 3], 3))

"COMBINING ARRAYS"

p = np.ones([2, 3], int)
print(p)

# Use vstack to stack arrays in sequence vertically (row wise).
print(np.vstack([p, 2*p]))

# Use hstack to stack arrays in sequence horizontally (column wise).
print(np.hstack([p, 2*p]))

"OPERATIONS"
# Use +, -, *, / and ** to perform element wise addition,
# subtraction, multiplication, division and power.

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)

print(x - y)

print(x * y)

print(x / y)

print(x**2)  # elementwise power  [1 2 3] ^2 =  [1 4 9]
print(x**y)

# Dot product
x.dot(y)  # dot product  1*4 + 2*5 + 3*6

# create a new array using a previous array y and its squared values.
z = np.array([y, y**2])
print(z)

print(len(z))  # number of rows of array

"TRANSPOSING"  # Transposing permutes the dimensions of the array.
z = np.array([y, y**2])
# The shape of array z is (2,3) before transposing.
print(z.shape)
# Use .T to get the transpose.
print(z.T)
# The number of rows has swapped with the number of columns.
print(z.T.shape)

"DATA TYPE"
# Use .dtype to see the data type of the elements in the array.
print(z.dtype)

# Use .astype to cast to a specific type.
z = z.astype('f')
print(z.dtype)

"MATH FUNCTIONS"
# Numpy has many built in math functions that can be performed on arrays.
a = np.array([-4, -2, 1, 3, 5])

print(a.sum())

print(a.max())

print(a.min())

print(a.mean())

print(a.std())  # standard deviation

# argmax and argmin return the index of the maximum and minimum values in the array.

print(a.argmax())

print(a.argmin())
