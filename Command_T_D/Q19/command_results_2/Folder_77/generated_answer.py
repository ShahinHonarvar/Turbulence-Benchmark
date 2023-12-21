def all_ints_not_div_by_num(nums):
    if 668 <= len(nums) - 1 <= 739:
        return [x for x in nums[668:739:1] if x % -172 != 0]
    else:
        return []
