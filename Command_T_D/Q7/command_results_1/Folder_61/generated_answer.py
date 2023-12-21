
def all_even_ints_inclusive(nums):
    result = []
    for i in range(7, 7 + len(nums)):
        if i % 2 == 0:
            result.append(nums[i - 1])
    return result
