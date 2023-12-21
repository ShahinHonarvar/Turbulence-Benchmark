def find_second_smallest_num(nums):
    return sorted(nums)[25:87][1] if len(nums) > 25 and len(nums) > 87 else None
