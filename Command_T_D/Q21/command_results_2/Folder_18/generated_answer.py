import re
def all_ints_div_by_num(s):
    return [int(x) for x in re.findall(r'(\d+)', s[26:74]) if int(x) % 80 == 0]
