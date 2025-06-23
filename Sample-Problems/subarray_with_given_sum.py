# How to solve the problem in an interview
arr0 = [1, 7, 4, 2, 1, 3, 11, 5]
target0 = 10
output0 = 2, 6

def subarray_sum(arr, target):
    pass

"""
1. Generic array where the subarray is in the center
2. Subarray could be at the start
3. Subarray could be at the end
4. There is no subarray that adds up to 10
5. You have a few zeros in the list
6. There are multiple subarrays with the same sum
7. The array is empty
8. The subarray is a single element
"""

# Brute force solution (Complexity-(n^3))
def subarray_sum1(arr, target):
    n = len(arr)
    # i goes from 0 to n - 1
    for i in range(0, n):
        # j goes from i to n
        for j in range(i, n + 1):
            # check if the sum of the subarray is equal to target
            if (sum(arr[i:j]) == target):
                # answer found
                return i, j
    return None, None

arr = [1, 7, 4, 2, 1, 3, 11, 5]
target = 19
print(subarray_sum1(arr, target))

# Apply optimization
## maintain a running sum for inner loop
## when sum exceeds target, break inner loop
# (Complexity - (n^2))
def subarray_sum2(arr, target):
    n = len(arr)
    # i goes from 0 to n - 1
    for i in range(0, n):
        s = 0 # running sum
        for j in range(i, n + 1):
            if s == target:
                return i, j
            elif s > target:
                break
            if j < n:
                s += arr[j]
    return None, None

# Complexity - (n)
def subarray_sum3(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and j < n + 1:
        if s == target:
            return i, j
        elif s < target:
            if j < n:
                s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None

arr = [1, 7, 4, 2, 1, 3, 11, 5]
target = 19
print(subarray_sum3(arr, target))