
def insert_at_index(nums):
    result = [0]*(len(nums)+1)
    for i in range(len(nums)):
        result[i+1] = nums[i]
    result[30] = 37
    return result
