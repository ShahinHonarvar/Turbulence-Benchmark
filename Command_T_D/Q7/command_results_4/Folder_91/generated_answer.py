
def all_even_ints_inclusive(nums):
    result = []
    for index in range(len(nums) - 1):
        if nums[index] % 2 == 0:
            result.append(nums[index])
            result.append(nums[index + 1])
            break
    return result
