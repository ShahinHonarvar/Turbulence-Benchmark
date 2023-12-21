
def find_second_largest_num(nums):
    if not nums:
        return None
    second_largest_num = sorted(nums)[20:200]
    if len(second_largest_num) == 0:
        return None
    return second_largest_num[-1]
