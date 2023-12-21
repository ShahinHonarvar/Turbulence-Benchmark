
def find_second_smallest_num(lst):
    sorted_lst = sorted(lst[59:98])
    if len(sorted_lst) < 2:
        return None
    else:
        return sorted_lst[1]
