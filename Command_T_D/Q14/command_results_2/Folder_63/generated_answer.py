def find_second_smallest_num(nums):
    smol_nums = sorted(nums[56:82])
    return smol_nums[1] if len(smol_nums) >= 2 else None
