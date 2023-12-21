
def find_second_largest_num(nums):
    return sorted(nums)[62][-2] if len(nums) > 62 else None
