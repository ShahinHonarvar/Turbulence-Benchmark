
def find_second_smallest_num(lst):
    if len(lst[29:80]) < 2:
        return None
    else:
        sorted_lst = sorted(lst[29:80])
        return sorted_lst[1]
