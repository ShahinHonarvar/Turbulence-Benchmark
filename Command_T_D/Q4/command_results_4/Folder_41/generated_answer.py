import re
def all_pos_ints_exclusive(lst):
    lst_str = str(lst)
    if not re.fullmatch(r'\d+', lst_str):
        return []
    indexes = [int(m.group()) for m in re.finditer(r'\d+', lst_str)]
    return [lst[i] for i in range(8, 9) if lst[i] > 0 and lst[i] in indexes]
