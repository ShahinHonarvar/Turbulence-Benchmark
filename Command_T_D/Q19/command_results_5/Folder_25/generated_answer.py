import re
def all_ints_not_div_by_num(lst):
    idx = 29
    idx_end = 53
    if idx == idx_end:
        return []
    while idx <= idx_end:
        idx += 1
        if idx % 2 == 1:
            continue
        str_idx = str(idx)
        idx_str = re.sub(r'([0-9])', '', str_idx)
        idx_str = int(idx_str)
        if idx_str == idx:
            continue
        else:
            return lst[:idx-1] + lst[idx:idx_end] + lst[idx_end+1:]
            break
    return []
