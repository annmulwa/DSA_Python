# input
str1 = "intention"
str2 = "execution"

# output
output1 = 5

# function signature
def min_steps1(str1, str2):
    pass

# test cases
"""
1. general case (listed above)
2. no change is required
3. all the characters need to be changed
4. strings of equal length
5. strings of unequal length
6. one of the strings is empty
7. only deletion, only addition, only swapping
"""

# using recursion to solve the problem
"""
Recursion:
- If the first character is equal, then ignore from both
- If the first character is not equal
    - Either it has to be delete
        - 1 + recursively solve after ignoring the first character of str1
    - or swapped
        - 1 + recursively solve after ignoring the first character of both strings
    - or a character inserted before
        - 1 + recursively solve after ignoring the first character of str2
"""

# we will need pointers to prevent additional memory allocation
# Time complexity - (O(3^min(m,n))) where m and n respresent the length of the 2 strings
def min_steps(str1, str2, i1=0, i2=0):
    if i1 == len(str1):
        return len(str2) - i2
    elif i2 == len(str2):
        return len(str1) - i1
    elif str1[i1] == str2[i2]:
        return min_steps(str1, str2, i1 + 1, i2 + 1)
    else:
        return 1 + min(min_steps(str1, str2, i1 + 1, i2),     # deleted
                       min_steps(str1, str2, i1 + 1, i2 + 1), # swapped/replaced
                       min_steps(str1, str2, i1, i2 + 1))     # inserted

print(min_steps('intention', 'execution'))

# using memoization
# Complexity (n1 * n2)
def min_steps_memo(str1, str2):
    memo ={}

    def recurse(i1=0, i2=0):
        key = (i1, i2)
        if key in memo:
            return memo[key]
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1 + 1, i2 + 1)
        else:
            memo[key] = 1 + min(recurse(i1 + 1, i2),
                                recurse(i1 + 1, i2 +1),
                                recurse(i1, i2 + 1))
        return memo[key]
    return recurse(0, 0)

print(min_steps_memo('intention', 'execution'))
print(min_steps_memo('abcdef', 'azced'))

# using dynamic programming
