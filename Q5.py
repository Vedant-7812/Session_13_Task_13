#Q.5)
import numpy as np
# a) 1D array of 10 random numbers between 0 and 1
arr1 = np.random.rand(10)
# b) 3x3 matrix of random numbers from standard normal distribution
arr2 = np.random.randn(3, 3)
# c) 4x5 matrix of random integers between 10 and 50
arr3 = np.random.randint(10, 51, (4, 5))
# Print all arrays
print("a) 1D Array of 10 Random Numbers (0 to 1):")
print(arr1)
print("\nb) 3x3 Matrix of Random Numbers (Standard Normal Distribution):")
print(arr2)
print("\nc) 4x5 Matrix of Random Integers (10 to 50):")
print(arr3)
