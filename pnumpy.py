import numpy as np

# Array Creation and Attributes
array = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
])
print('Shape of the array:', array.shape)
print('Number of dimensions:', array.ndim)
print('Total number of elements:', array.size)
print('Data type of the array:', array.dtype)
print('Access specific element:', array[0, 0, 2])

# Data Type Handling
convertion = np.array([[1, 2, 3], [4, 'Hi', 6], [7, 8, 9]])
print('Specific element:', convertion[1, 1])
print('Data type of row 1:', convertion[1].dtype)

# Array Initialization
a = np.full((3, 3, 4), 9)
print('Full array:\n', a)

b = np.zeros((2, 5, 5))
print('Zeros array:\n', b)

c = np.ones((2, 5, 10))
print('Ones array:\n', c)

d1 = np.empty((2, 2, 2))
print('Empty array:\n', d1)

e = np.arange(0, 100, 2)
print('Range array:\n', e)

# Special Values
print('NaN (Not a Number):', np.nan)
print('Infinity:', np.inf)
print('Check NaN in sqrt(-1):', np.isnan(np.sqrt(-1)))
print('Check Infinity:', np.isinf(np.array([10]) / 0))

# Mathematical Operations
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
a1 = np.array(l1)
a2 = np.array(l2)

print('Element-wise multiplication:', a1 * 5)
print('Element-wise addition:', a1 + 5)
print('List concatenation:', l1 + l2)
print('Array addition:', a1 + a2)
print('Element-wise division:', a1 / a2)
print('Element-wise subtraction:', a1 - a2)

# Array Manipulation
b1 = np.array([1, 2, 3])
b1 = np.append(b1, [7, 8, 9])
print('Appended array:', b1)

b1 = np.insert(b1, 3, [10, 11, 12])
print('Inserted array:', b1)

c1 = np.array([[1, 2, 3], [4, 5, 6]])
print('Original array:\n', c1)
print('Array after deleting row 1:\n', np.delete(c1, 1, axis=0))

# Reshaping and Flattening
d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print('Original array:\n', d)
print('Transposed array:\n', d.T)
print('Reshaped (5x4):\n', d.reshape(5, 4))
print('Flattened array:', d.flatten())
print('Ravel (view) of array:', d.ravel())

flattened = d.flatten()
flattened[1] = 200
print('Modified flattened array:', flattened)
print('Original array remains unchanged:\n', d)

raveled = d.ravel()
raveled[1] = 400
print('Modified ravel array:', raveled)
print('Original array also updated:\n', d)

# Axis Swapping
a3 = np.arange(8).reshape(2, 2, 2)
print('Original 3D array:\n', a3)

swapped = np.swapaxes(a3, 0, 2)
print('Swapped axes:\n', swapped)

# Array Concatenation
f1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
f2 = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
f = np.concatenate((f1, f2), axis=1)
f_0 = np.stack((f1, f2), axis=-1)
f_1 = np.hstack((f1, f2))
f_2 = np.vstack((f1, f2))

print('After concatenating:\n', f)
print('Stack along last axis:\n', f_0)
print('Horizontal stack:\n', f_1)
print('Vertical stack:\n', f_2)

# Random Numbers
number = np.random.randint(0, 100, size=(2, 3, 4))
print('Random array:\n', number)

# Reversing an Array
p = np.array([[1, 2, 3], [5, 6, 7]])
p_reversed = p[::-1]
print('Reversed array:\n', p_reversed)
