def all_ints_div_by_num(nums):
    return [i for i in range(4, len(nums), 3) if not (nums[i] % 3)]
