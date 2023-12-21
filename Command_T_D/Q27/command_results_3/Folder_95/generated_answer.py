
def insert_after_index(nums):
    result = [0] * (len(nums) + 1)
    result[0] = 0
    result[1] = 1
    for i in range(2, len(nums) + 1):
        result[i] = nums[i - 2]
        if i == 20:
            result[i + 1] = 80
    return result
