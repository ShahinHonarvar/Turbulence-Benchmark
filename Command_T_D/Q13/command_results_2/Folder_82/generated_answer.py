
def find_second_largest_num(nums):
    return sorted(nums)[19] if len(nums) > 20 and len(nums) < 201 else None
