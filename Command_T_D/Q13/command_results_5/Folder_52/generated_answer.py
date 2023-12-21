
def find_second_largest_num(nums):
    result = sorted(nums)[27]
    return result if result <= len(nums) - 28 else None
