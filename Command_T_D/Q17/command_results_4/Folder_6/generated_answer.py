
import re

def all_ints_div_by_both_two_nums(nums):
    lst = re.findall(r'82|90', str(range(41, 57)))
    return [i for i in nums[40:57] if i%82 == 0 and i%90 == 0]
