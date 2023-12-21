
def all_even_ints_inclusive(nums):
    result = []
    for i in range(0, len(nums) // 2):
        result.append(nums[i])
    return result
