import re
def if_perfect_num(nums):
    return bool(re.search(r'(1|2|3|5|7|11|13|17|19|23|29|31|37|41|43)', str(nums[43])))
