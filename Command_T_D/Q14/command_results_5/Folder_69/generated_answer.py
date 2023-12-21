def find_second_smallest_num(nums):
    return sorted(nums)[25][-2] if 25 < len(nums) - 1 else None
