# Mocking the guess API for local testing
def guess(num):
    if num == picked_number:
        return 0
    elif num > picked_number:
        return -1
    else:
        return 1
# LINEAR SEARCH SOLUTION
# def guessNumber(n):
#     num = 1

#     while num <= n:
#         res = guess(num)
#         if res == 0:
#             return num
#         num += 1

# BINARY SEARCH SOLUTION
def guessNumber(n):
    low, high = 1, n

    while low <= high:
        mid = (low + high) // 2
        res = guess(mid)

        if res == 0:
            return mid
        elif res == -1:
            high = mid - 1
        elif res == 1:
            low = mid + 1

picked_number = 6  # <-- set the number you want to guess
n = 10
print(guessNumber(n))