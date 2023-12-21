def find_second_largest_num(nums):
    return sorted(nums)[10:100][1] if len(nums) > 9 else None
