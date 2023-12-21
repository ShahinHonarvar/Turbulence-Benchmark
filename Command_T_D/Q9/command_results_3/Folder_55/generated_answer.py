def all_odd_ints_inclusive(nums):
    result = [x for x in range(10, len(nums) + 1, 2) if nums[x-10] % 2 == 1]
    return result
