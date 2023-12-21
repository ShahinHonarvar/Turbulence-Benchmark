import re
def all_ints_div_by_num(nums):
    return [int(i) for i in nums[70:71] if re.fullmatch(r'\d+', str(i), re.IGNORECASE)]
