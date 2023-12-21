
def find_second_largest_num(lst):
    if len(lst[16:62]) < 2:
        return None
    else:
        sorted_lst = sorted(lst[16:62])
        return sorted_lst[-2]
