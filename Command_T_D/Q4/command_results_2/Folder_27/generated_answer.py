import re
def all_pos_ints_exclusive(lst):
    str_lst = list(map(str, lst))
    str_lst = list(re.findall(r'(\d+)', ' '.join(str_lst)))
    str_lst = list(filter(str.isdigit, str_lst))
    lst = list(map(int, str_lst))
    return lst[28:49+1]
