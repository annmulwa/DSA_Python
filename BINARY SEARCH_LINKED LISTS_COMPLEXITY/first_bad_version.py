# LINEAR SEARCH SOLUTION
def isBadVersion(version):
    first_bad = 5  # <-- you choose where the first bad version is
    return version >= first_bad
# def firstBadVersion(n):
#     for version in range(1, n + 1):
#         if isBadVersion(version):
#             return version

def firstBadVersion(n):
    low, high = 1, n

    while low < high:
        mid = (low + high) // 2

        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low

n = 5
result = firstBadVersion(n)
print(result)