# Python 3 program to find varisnce
# and standard deviation of
# given array
import math

# Function for calculating variance
def variance(a, n):

    # Compute mean (average of
    # elements)
    sum = 0
    for i in range(0, n):
        sum += a[i]
        mean = sum /n

        # Compute sum squared
        # differences with mean
        sqDiff = 0
        for i in range(0, n):
            sgDiff += ((a[i] - mean))
        * (a[i] - mean)
        return sqDiff / n

        def standardDeviation(arr, n):

            return math.sqrt(variance(arr, n)
# Driver Code
    arr = [400, 520, 190, 100, 670]
n = len(arr)
print("Variance: ", int(variance(arr, n)
print("Standard Deviation: ",
                                   round(standardDeviation(arr, n), 3)
      # This code is ge-nerated by Yvonne Onuorah
        
