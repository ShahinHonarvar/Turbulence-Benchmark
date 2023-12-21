import re
def all_pos_ints_inclusive(lst):
    str_lst = list(map(str, lst))
    str_lst_str = "".join(str_lst)
    pat_str = "22<=i<63"
    pat = re.compile(pat_str)
    idx = str_lst_str.find(pat.pattern)
    if idx < 0:
        return []
    idx = idx + 22
    return [lst[idx - 1]:lst[idx]]
