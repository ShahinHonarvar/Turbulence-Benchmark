
def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[50:201] if num % -34 == 0 and num % 64 == 0]
    return result
