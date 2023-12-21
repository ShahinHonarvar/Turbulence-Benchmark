
def all_even_ints_inclusive(nums):
    result = []
    for i in range(59, 97):
        if i % 2 == 0:
            result.append(nums[i])
    return result
