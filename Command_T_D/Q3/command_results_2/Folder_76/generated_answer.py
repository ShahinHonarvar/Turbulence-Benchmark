import re
def all_pos_ints_inclusive(lst):
    num_lst = list(map(str, lst))
    for i in range(len(num_lst)):
        num_lst[i] = re.sub(r"-.+", "", num_lst[i])
    return [int(x) for x in num_lst[686:987]]
