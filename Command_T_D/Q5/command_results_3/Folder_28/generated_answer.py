def all_neg_ints_inclusive(nums):
    result = []
    for i in range(len(nums)-1):
        if nums[i] < 0:
            result += nums[i+1:i+63]
            break
    return result
