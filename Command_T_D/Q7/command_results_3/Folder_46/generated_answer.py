
def all_even_ints_inclusive(nums):
    result = []
    for i in range(30, 87, 2):
        if i in nums:
            result.append(i)
    return result
