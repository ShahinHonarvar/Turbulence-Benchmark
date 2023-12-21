import re
def all_pos_ints_exclusive(lst):
    idx_str = "27-34"
    idx_list = re.findall(r'\d+', idx_str)
    idx_list = list(set(idx_list))
    idx_list = sorted(idx_list)
    idx_list = idx_list[1:] + [int(idx_list[0])]
    idx_list = idx_list[1:-1]
    return [idx for idx in range(27, 34) if idx in idx_list]
