def hasDuplicate(nums):
    new_set=set()
    for num in nums:
        if num in new_set:
            return True
        new_set.add(num)
    return False



nums = [1, 2, 3, 4]
result = hasDuplicate(nums)
print(result)