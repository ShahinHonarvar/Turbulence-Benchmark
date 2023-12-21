def all_neg_ints_exclusive(nums):
    if not nums:
        return []
    if 70 <= len(nums) and len(nums) <= 200:
        negative_nums = nums[70:-1]
        if negative_nums:
            return negative_nums
    return []
