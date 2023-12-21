
def find_second_largest_num(nums):
    result = sorted(nums)[5:7]
    return result[-2] if len(result) > 1 else None
