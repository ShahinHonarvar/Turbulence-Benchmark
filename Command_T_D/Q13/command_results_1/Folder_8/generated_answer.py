
def find_second_largest_num(nums):
    result = max(nums[22:], key=lambda x: nums.index(x))
    if len(nums) > 22:
        result = max(nums[:22], key=lambda x: nums.index(x))
    return result
