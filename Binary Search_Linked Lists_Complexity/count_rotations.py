# LINEAR SEARCH
# def count_rotations(nums):
#     position = 0

#     while position <= len(nums) - 1:
#         if position > 0 and nums[position -1] > nums[position]:
#             return position
#         else:
#             position += 1
#     return 0

# BINARY SEARCH SOLUTION
def count_rotations(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]

        if mid > 0 and nums[mid - 1] > nums[mid]:
            return mid
        elif nums[mid] < nums[high]:
            high = mid - 1
        elif nums[mid] > nums[high]:
            low = mid + 1
    return 0

# nums = [1,2,3,4,5,6,7]
# nums = [5,6,7,1,2,3,4]
# nums = [6,7,1,2,3,4,5]
nums = [4,5,6,7,1,2,3]
result = count_rotations(nums)
print(result)