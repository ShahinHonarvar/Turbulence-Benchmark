import re
def all_pos_ints_exclusive(nums):
    s = str(range(0, len(nums) + 1))
    return [int(x) for x in re.findall(r'<[0-9]+>[0-9]+>', s)]
