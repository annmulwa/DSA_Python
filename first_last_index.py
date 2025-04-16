def first_index(nums, target):
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]

        print(f"low: {low}, high: {high}, mid: {mid}, mid_number: {mid_number}")

        if mid_number == target:
            # if mid - 1 >= 0 and nums[mid - 1] == target:
            result = mid
            high = mid - 1
        elif mid_number > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

def last_index(nums, target):
    low, high = 0, len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]

        print(f"low: {low}, high: {high}, mid: {mid}, mid_number: {mid_number}")

        if mid_number == target:
            # if mid + 1 <= len(nums) - 1 and nums[mid + 1] == target:
            result = mid
            low = mid + 1
        elif mid_number > target:
            high = mid - 1
        else:
            low = mid + 1
    return result

def first_last_index(nums, target):
    return [first_index(nums, target), last_index(nums, target)]

nums = [5, 7, 8, 8, 8, 8]
target = 8

result = first_last_index(nums, target)
print(result)