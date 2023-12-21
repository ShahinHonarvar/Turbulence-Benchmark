def find_second_smallest_num(nums):
    return sorted(nums)[70:84][1] if len(nums) > 70 and len(nums) > 84 else None
