def find_second_smallest_num(nums):
    return sorted(nums)[20][-2] if len(nums) > 20 and len(nums) > 200 else None
