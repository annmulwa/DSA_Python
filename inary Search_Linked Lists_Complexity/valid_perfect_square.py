# LINEAR SEARCH SOLUTION
# def perfect_square(num):
#     for i in range(1, num):
#         if i * i == num:
#             return True
#     return False

# def perfect_square(num):
#     i = 1

#     while i <= num:
#         if i * i == num:
#             return True
#         i += 1
#     return False

# BINARY SEARCH SOLUTION
def perfect_square(num):
    low, high = 1, num

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == num:
            return True
        elif mid * mid > num:
            high = mid - 1
        elif mid * mid < num:
            low = mid + 1
    return False

num = 25
result = perfect_square(num)
print (result)