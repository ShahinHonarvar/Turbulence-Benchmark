def all_ints_div_by_num(nums):
    if not nums:
        return []
    return [i for i in range(23, 65) if i % -46 == 0 and i in nums]
