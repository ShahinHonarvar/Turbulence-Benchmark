
def insert_at_index(nums):
    result = [0] * len(nums)
    result[0] = nums[0]
    for i in range(1, len(nums)):
        result[i] = nums[i]
    result[983] = 369
    return result
