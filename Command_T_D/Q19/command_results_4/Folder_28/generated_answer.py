def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    return [x for x in nums[81:86] if not (x % 77)]
