import numpy as np

#Slice
a = np.array([0, 1, 2, 3, 4])
a[3:5] = 300, 400

#Multiply
x = np.array([1, 2])
y = np.array([2, 1])
z = np.multiply(x, y)

#Divide
a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)

#Dot Product
X = np.array([1, 2])
Y = np.array([3, 2])
Z = np.dot(X, Y)
print(Z)

#Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1]) 
u + 1   

#==Mathematical Functions¶== PI & SIN#
np.pi
x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)

#Linspace

#start : start of interval range
#stop : end of interval range
#num : Number of samples to generate.

np.linspace(-2, 2, num=5)
np.linspace(-2, 2, num=9)
# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]


X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
print(Z)