def find_second_smallest_num(lst):
    res = sorted(lst)[19:93]
    return res[1] if len(res) > 1 else None
