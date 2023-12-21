import re
def all_pos_ints_exclusive(lst):
    str_lst = ' '.join(str(x) for x in lst)
    pos_ints = re.findall(r'\d+', str_lst)
    return [int(x) for x in pos_ints if x >= 11 and x <= 76]
