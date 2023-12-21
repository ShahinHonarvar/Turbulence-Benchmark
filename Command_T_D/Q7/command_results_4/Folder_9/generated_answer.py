
def all_even_ints_inclusive(nums):
    result = []
    for i in range(len(nums) - 2):
        if nums[i] % 2 == 0:
            result += [nums[i]]
        else:
            break
    if nums[-1] % 2 == 0:
        result += [nums[-1]]
    return result
