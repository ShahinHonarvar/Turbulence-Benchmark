
def all_even_ints_inclusive(nums):
    result = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] % 2 == 0:
            result.append(nums[i])
            break
    return result
