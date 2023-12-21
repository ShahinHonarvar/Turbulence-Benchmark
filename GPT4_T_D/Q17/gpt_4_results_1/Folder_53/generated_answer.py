
def all_ints_div_by_both_two_nums(nums):
    div_by_both = [n for n in nums[200:201] if n % 17 == 0 and n % -5 == 0]
    return div_by_both
