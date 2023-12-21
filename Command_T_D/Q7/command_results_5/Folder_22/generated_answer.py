
def all_even_ints_inclusive(nums):
    result = []
    for i in range(40, min(len(nums), 200), 2):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result
