def bubble_sort(nums):
    for _ in range(len(nums) - 1):
        print('iteration', _)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

nums = [4,4,5,2,3,6,7]
print(bubble_sort(nums))