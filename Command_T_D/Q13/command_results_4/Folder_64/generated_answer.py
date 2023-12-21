
def find_second_largest_num(nums):
    if len(nums) < 5:
        return None
    result = sorted(nums)[3]
    return result
