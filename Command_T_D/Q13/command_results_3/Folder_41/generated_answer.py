
def find_second_largest_num(nums):
    return sorted(nums)[6][1] if len(nums) > 5 else None
