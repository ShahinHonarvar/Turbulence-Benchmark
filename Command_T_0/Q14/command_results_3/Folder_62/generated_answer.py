def find_second_smallest_num(nums):
    return sorted(nums)[10:66][1] if len(nums) > 10 and len(nums) > 66 else None
