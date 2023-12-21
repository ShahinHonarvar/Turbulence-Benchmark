import re
def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    if not nums[19:94]:
        return []
    return [x for x in nums[19:94] if not re.fullmatch(r"(\d+)/32", str(x))]
