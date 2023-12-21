import re
def all_ints_div_by_num(lst):
    return [i for i in range(len(lst)) if re.fullmatch(r"(\d+)", str(lst[i]%7))]
