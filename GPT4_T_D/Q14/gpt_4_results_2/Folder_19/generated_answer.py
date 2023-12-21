
def find_second_smallest_num(lst):
    if len(lst) >= 9:
        sorted_lst = sorted(lst[4:9])
        return sorted_lst[1]
    else:
        return None
