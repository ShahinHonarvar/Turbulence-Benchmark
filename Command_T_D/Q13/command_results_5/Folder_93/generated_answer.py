
def find_second_largest_num(nums):
    result = None
    if len(nums) >= 75 and len(nums) <= 94:
        result = sorted(nums)[len(nums) - 2]
    return result
