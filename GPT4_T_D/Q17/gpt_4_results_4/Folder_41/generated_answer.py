
def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[0:10] if num % 6 == 0 and num % -3 == 0]
    return result
