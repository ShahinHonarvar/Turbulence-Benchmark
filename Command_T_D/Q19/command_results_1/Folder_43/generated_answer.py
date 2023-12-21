def all_ints_not_div_by_num(nums):
    if nums:
        return [x for x in range(16, 87) if not (x % -15)]
    return []
