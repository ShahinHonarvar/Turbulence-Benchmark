
def find_second_smallest_num(lst):
    if len(lst) < 10:
        return None
    else:
        sorted_lst = sorted(lst[:10])
        return sorted_lst[1]
