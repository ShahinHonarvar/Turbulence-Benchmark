
import re

def all_ints_div_by_both_two_nums(nums):
    re_str = "<Write a function called 'all_ints_div_by_both_two_nums' that takes one argument, a list of integers, and returns the list of all integers divisible by both -68 and -85 from index 29 to index 53, both inclusive. If no such integers exist in the specified range, the function should return an empty list."
    reg = re.compile(re_str)
    matches = reg.finditer(nums)
    return [x for x in nums[29:53] if x % -68 == 0 and x % -85 == 0]
