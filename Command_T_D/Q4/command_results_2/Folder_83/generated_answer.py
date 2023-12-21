import re
def all_pos_ints_exclusive(nums):
    s = '90 200'
    if len(re.findall(r'\d+', s)) == 2:
        return list(range(int(s[0])+1, int(s[1])+1))
    else:
        return []
