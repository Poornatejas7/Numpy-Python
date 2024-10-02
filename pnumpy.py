import numpy as np
array = np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                   [[11,22,33],
                   [44,55,66],
                   [77,88,99]]])
                  # [100,1000,101]]])
print('The dimension of array:',array.shape)
print('Deepnes of dimension :',array.ndim)
print('Size (number of elements inside the array) of array:',array.size)
print('The datatype is : ',array.dtype)
print(array[0,0,2])

#-----Data type---------

convertion = np.array([[1,2,3],
                       [4,'Hii','6'],
                       [7,8,9]])
print(convertion[1,1])
print(convertion[1].dtype)

#------Filling Array ----------

a = np.full((3,3,4),9)
print('full((3,3,4),9) : ',a)
print()

b = np.zeros((2,5,5))
print('Zeros(2,5,5) : ',b)

print()
c = np.ones((2,5,10))
print('ones(2,5,10) : ',c)
print()

d1 = np.empty((2,2,2))
print('Empty(2,2,2) : ',d1)
print()

e = np.arange(100)
print('Arrange(0,100,2) : ',e)
print()

print(np.nan) #not a number
print(np.inf) # infinity
print(np.isnan(np.sqrt(-1)))
print(np.isinf(np.array([10] ) / 10))

#------Mathematiacl operater--------

l1  = [1,2,3,4,5]
l2 =  [6,7,8,9,10]

a1 = np.array([l1])
a2 = np.array([l2])

# Recursion opereater (*)
print(f'It gives recursion values in list : {l1*5}')
print(f'It gives value of array which is multiplied by each element : {a1*5}')

# addition  operater
#print(f'It does not give element which is multipliesd by each elemeny (Gives error) : {l1+5}')
print(f'It gives the values of each element which is added : {a1+5}')

#Concatination
print(f'Concatinating 2 list : {l1+l2}')
print(f'Cancatinating 2 arrays (it adds to coresponding elements of an array) : {a1+a2}')

#division
print(f'Array supports division operater :{a1/a2}')

#subtraction
print(f'Array supports subtraction operater : {a1-a2}')

# Multi dimensioned array operations
b = np.array([[1,2,3],
              [4,5,6]])

c = np.array([[7,8,9],
              [10,11,12]])

print('Multi dimensioned array division : ',b/c)

#--------Array methods------

b1 = np.array([1,2,3])
print('The value of b1 :',b1)
b1 = np.append(b1,[7,8,9])
print('Appended value  : ',b1)
b1 = np.insert(b1,3,[10,11,12])

print('Inserted value : ',b1)

c1 = np.array([[1,2,3],
              [4,5,6]])
print('The value of c1 :',c1)
#print('The value after deleting :',np.delete(c1,1)) # delete the eleents at that index
#print('The value after deleting :',np.delete(c1,[1,3])) # delete the
print('The value after deleting :',np.delete(c1,1,0)) # delete the

# ---- Structureing methods --------

d = np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20]])
print('The value of d :',d)
print('The value of d :',d.T) # transpose the array
print('Shape is : ', d.shape)
print('Reshape (5,4): ',d.reshape((5,4)))
print('Reshape (2,2,5): ',d.reshape((2,2,5)))
print('Reshape : ',d.reshape((20,1)))
print('Flattning : ',d.flatten())
print('Flattning shape : ',d.flatten().shape) # shape of flattened array
print('Ravel : ', d.ravel())

var1 = d.flatten() # Flatten() provides only copy so it will not make any changes in original array
var1[1] = 200
print('Flattened array : ',var1)
print('Orignal array : ',d)

var2 = d.ravel() # Ravel() does not provide copyied array so it makes changes in original array
var2[1] = 400
print('Ravel array : ',var2)
print('Original array : ' ,d)

print('Swaping axis : ',d.swapaxes(0,1))



# Create a 3D array (a 2x2x2 cube)
a3 = np.arange(8).reshape(2, 2, 2)
print("The original 3D array:")
print(a3)

# Swap numbers between axis 0 (depth) and axis 2 (width)
swapped_a = np.swapaxes(a3, 2, 0)
print("\nThe array after applying the swapaxes function:")
print(swapped_a)

#Concatinating
f1 = np.array([[1,2,3,4,5],
               [6,7,8,9,10]])

f2 = np.array([[11,12,13,14,15],
               [16,17,18,19,20]])
f = np.concatenate((f1,f2),axis=1) 
f_0 =np.stack((f1,f2),axis=-1) 
f_1 =np.hstack((f1,f2)) 
f_2 =np.vstack((f1,f2)) 
print('After concatinanting : ',f)
print()
print('The value after stack : ',f_0)
print()
print('The value after vstack : ', f_1)
print()
print('The value after hstack : ', f_2)


number = np.random.randint(0,100,size=(2,3,4))
print('The value of random : ',number)
n = np.stack((number))
print()
print('The value of n : ',n)


p = np.array([[1,2,3],
             [5,6,7]])
p.reverse()
print('The value of reverse',p)