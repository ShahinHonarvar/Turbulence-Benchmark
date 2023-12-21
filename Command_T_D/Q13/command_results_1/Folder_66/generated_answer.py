
def find_second_largest_num(nums):
    second_largest_num = None
    if len(nums) > 49:
        second_largest_num = sorted(nums)[49]
    return second_largest_num
