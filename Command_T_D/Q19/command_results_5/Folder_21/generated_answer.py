import re
def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    if not isinstance(nums, list):
        return []
    result = []
    for x in nums[469:566]:
        if not re.match(r'([13579])([13579])([13579])', str(x)):
            result.append(x)
    return result
