
def find_second_largest_num(nums):
    return sorted(nums)[10:66][-2] if len(nums) > 10 and len(nums) > 66 else None
