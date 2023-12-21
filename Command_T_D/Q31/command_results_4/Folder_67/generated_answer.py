import re
def if_perfect_num(nums):
    return re.search(r'(1099\d)', str(nums[43])).group() == '1099'
