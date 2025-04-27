def search_rotated_array(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]

        if mid_number == target:
            return mid

        if nums[low] <= mid_number:
            if nums[low] <= target < mid_number:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[low] >= mid_number:
            if mid_number < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
# nums = [6,7,0,1,2,4,5]
target = 0

result = search_rotated_array(nums, target)
print(result)