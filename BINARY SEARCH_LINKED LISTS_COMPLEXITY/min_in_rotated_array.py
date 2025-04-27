def find_min_num(nums):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) - 1
        mid_number = nums[mid]

        if mid > 0 and nums[mid - 1] > nums[mid]:
            return mid_number
        elif mid_number > nums[high]:
            low = mid + 1
        elif mid_number < nums[high]:
            high = mid - 1
    return nums[0]

# nums = [5,1,2,3,4]
nums = [2,3,4,5]
result = find_min_num(nums)
print(result)