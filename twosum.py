def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate (nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i



nums = [3,4,5,6]
target = 8

result = twoSum(nums, target)
print(result)