def find_second_smallest_num(nums):
    return sorted(nums)[75:88][1] if len(nums) > 88 else None
