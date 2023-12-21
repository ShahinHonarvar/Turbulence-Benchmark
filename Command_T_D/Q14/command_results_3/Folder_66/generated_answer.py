def find_second_smallest_num(nums):
    return sorted(nums)[-2] if len(nums) > 60 and len(nums) < 100 else None
