
def all_even_ints_inclusive(nums):
    result = []
    for i in range(0, 7):
        if i % 2 == 0:
            result.append(nums[i])
    return result
