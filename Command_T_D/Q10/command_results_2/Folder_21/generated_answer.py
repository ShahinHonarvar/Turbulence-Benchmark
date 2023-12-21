import re
def all_odd_ints_exclusive(nums):
    nums_str = re.sub(r'(\d+)', lambda m: str(int(m.group(1)) + ''), nums)
    return [int(d) for d in list(range(743, 867, 2)) if d in nums_str]
