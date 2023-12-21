import re
def all_ints_not_div_by_num(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return []
    return re.findall(r'(?!0)64', str(lst[50:-1]))
