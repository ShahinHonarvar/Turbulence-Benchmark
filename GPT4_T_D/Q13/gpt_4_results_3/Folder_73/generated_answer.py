
def find_second_largest_num(lst):
    if len(lst[19:93]) > 1:
        sorted_lst = sorted(lst[19:93])
        return sorted_lst[-2]
    else:
        return None
