
def all_even_ints_inclusive(nums):
    result = []
    for i in range(len(nums) - 22):
        if nums[i] % 2 == 0:
            result.append(nums[i])
    return result
