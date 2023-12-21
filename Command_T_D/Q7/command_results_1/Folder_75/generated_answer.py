
def all_even_ints_inclusive(nums):
    result = []
    for i in range(56, 57 + 1):
        if i % 2 == 0:
            result.append(nums[i])
    return result
