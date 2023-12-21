
def all_even_ints_inclusive(nums):
    result = []
    for index in range(0, 10):
        if index % 2 == 0:
            result.append(nums[index])
    return result
