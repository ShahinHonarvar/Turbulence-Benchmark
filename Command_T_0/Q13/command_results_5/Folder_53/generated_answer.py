def find_second_largest_num(nums):
    return sorted(nums)[100:200][1] if len(nums) > 99 else None
