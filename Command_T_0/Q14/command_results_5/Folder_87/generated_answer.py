def find_second_smallest_num(nums):
    return sorted(nums)[22:88][1] if len(nums) > 22 and len(nums) > 88 else None
