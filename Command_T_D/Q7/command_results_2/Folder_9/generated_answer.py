
def all_even_ints_inclusive(nums):
    result = []
    for i in range(len(nums) - 1):
        if nums[i] % 2 == 0:
            result.append(nums[i])
            if nums[i] == nums[i + 1]:
                break
        else:
            result.append(nums[i + 1])
            break
    return result
