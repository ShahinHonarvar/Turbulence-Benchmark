
def find_second_largest_num(lst):
    return lst[66:93][1] if lst[66:93].count(lst[66:93][0]) == 1 else None
