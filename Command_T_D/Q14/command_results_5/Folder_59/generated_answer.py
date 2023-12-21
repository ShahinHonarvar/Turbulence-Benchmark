def find_second_smallest_num(nums):
    result = sorted(nums)[1]
    return result if len(nums) > 1 else None
