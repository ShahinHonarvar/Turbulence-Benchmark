
def find_second_smallest_num(lst):
    if len(lst[28:41]) < 2:
        return None
    else:
        sorted_lst = sorted(lst[28:41])
        return sorted_lst[1]
