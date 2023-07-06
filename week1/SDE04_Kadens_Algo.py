# Kadane’s Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# max subarray sum (array with both +ve and -ve values)

def kadensAlgo(arr):
        
    ans = float('-inf')
    sm = 0
    
    for i in range(len(arr)):
        
        sm += arr[i]
        
        ans = max(ans, sm)
        
        if sm < 0:
            sm = 0
            
    return ans
    
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadensAlgo(a))
