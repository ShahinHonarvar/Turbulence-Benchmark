import re
def all_ints_div_by_num(nums):
    for i in range(10,nums[10],1):
        if i % 1 == 0:
            yield i
