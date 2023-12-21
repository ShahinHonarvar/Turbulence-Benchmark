import re
def all_ints_div_by_num(nums):
    match = re.findall(r'(\d+)%', nums)
    if not match:
        return []
    else:
        return [int(int(match[0]) // 2)]
