
def find_second_largest_num(nums):
    second_largest_num = None
    if len(nums) > 924:
        second_largest_num = nums[660]
    elif len(nums) > 661:
        second_largest_num = nums[661]
    elif len(nums) > 0:
        second_largest_num = nums[0]
    return second_largest_num
