
def find_second_largest_num(nums):
    second_largest_num = None
    if len(nums) >= 34 and len(nums) <= 55:
        sorted_nums = sorted(nums)
        second_largest_num = sorted_nums[len(sorted_nums) - 2]
    return second_largest_num
