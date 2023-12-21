def find_second_largest_num(nums):
    return sorted(nums)[21:97][1] if len(nums) > 20 else None
