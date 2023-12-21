
def all_even_ints_inclusive(nums):
    result = []
    for i in range(0, len(nums) + 1):
        if i % 2 == 0:
            result.append(nums[i - 1])
    return result
