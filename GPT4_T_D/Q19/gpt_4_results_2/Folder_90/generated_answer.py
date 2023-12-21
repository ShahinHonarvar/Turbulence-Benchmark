
def all_ints_not_div_by_num(nums):
    subset_nums = nums[768:905]
    result = [num for num in subset_nums if num % -430 != 0]
    return result
