def find_second_smallest_num(nums):
    return sorted(nums)[25:59][1] if len(nums) > 25 and len(nums) > 59 else None
