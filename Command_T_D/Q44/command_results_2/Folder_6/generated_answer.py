import re
def composite_nums_between_indices(nums):
    return set(nums[13:68]) - set(re.findall(r'(2|3|5|7|11)', str(nums)))
