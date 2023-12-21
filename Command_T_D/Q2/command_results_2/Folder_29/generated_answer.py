def all_ints_exclusive(nums):
    result = []
    for i in range(len(nums)-5):
        result += nums[i+86:i+89+1]
    return result
