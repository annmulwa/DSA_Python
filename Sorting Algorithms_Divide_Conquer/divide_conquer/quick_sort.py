def quick_sort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)

    return nums

def partition(nums, start=0, end=None):
    print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    l,r = start, end - 1

    while l < r:
        print('  ', nums, l, r)
        if nums[l] < nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    print('     ', nums, l, r)
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

# nums = [2,4,5,1,7,3]
nums = [2,3,4,1,6,9,7,8,0]
print(partition(nums))
print(quick_sort(nums))