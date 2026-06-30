#Q.9)
import numpy as np
# Generate a 1D array of 20 random integers between 1 and 50
arr = np.random.randint(1, 51, 20)
# Reshape into a 4x5 matrix
matrix = arr.reshape(4, 5)
# Print the matrix
print("4x5 Matrix:")
print(matrix)
# Print statistics
print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))
# Find maximum value in each row
print("\nMaximum Value in Each Row:")
print(np.max(matrix, axis=1))
