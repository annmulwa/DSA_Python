# LINEAR SEARCH SOLUTION
# def search_insert_position(nums, target):
#     position = 0

#     while position <= len(nums) - 1:
#         if nums[position] == target:
#             return position
#         elif nums[position] > target:
#             return position
#         # elif position == len(nums) - 1:
#         #     return position + 1
#         else:
#             position += 1
#     return position

# BINARY SEARCH SOLUTION
def search_insert_position(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]

        if mid_number == target:
            return mid
        elif mid_number > target:
            high = mid - 1
        elif mid_number < target:
            low = mid + 1
    return low

nums = [1,3,5,6]
target = 7
result = search_insert_position(nums, target)
print(result)