#Q.10)
import numpy as np
try:
    # Ask the user how many numbers to generate
    n = int(input("Enter how many random numbers you want to generate: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        # Generate random numbers between 10 and 100
        arr = np.random.randint(10, 101, n)
        # Print the array
        print("\nGenerated Array:")
        print(arr)
        # Statistics
        print("\nMean:", np.mean(arr))
        print("Median:", np.median(arr))
        print("Standard Deviation:", np.std(arr))
        print("Minimum:", np.min(arr))
        print("Maximum:", np.max(arr))
        # Reshape into a 2D array if possible
        if n % 2 == 0:
            matrix = arr.reshape(2, n // 2)
            print("\nReshaped 2D Array:")
            print(matrix)
            print("\nRow-wise Sum:")
            print(np.sum(matrix, axis=1))
        else:
            print("\nCannot reshape into a 2D array because the number of elements is odd.")
except ValueError:
    print("Invalid input! Please enter an integer.")
except Exception as e:
    print("Error:", e)
