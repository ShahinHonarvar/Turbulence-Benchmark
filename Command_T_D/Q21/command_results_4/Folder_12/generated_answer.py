def all_ints_div_by_num(nums):
    if 23 <= len(nums) <= 65:
        return [x for x in nums[23:-46] if x == x // -46]
    else:
        return []
