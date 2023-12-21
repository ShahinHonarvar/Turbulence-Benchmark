
def all_pos_ints_inclusive(nums):
    if not nums:
        return []
    else:
        return [num for num in nums[0:1] if num > 0]
