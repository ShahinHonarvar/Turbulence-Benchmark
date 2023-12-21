def all_ints_div_by_num(nums):
    return [nums[421:489] for i in range(4) if any(nums[i] for i in range(421, 489) if nums[i] % 885 == 0)]
