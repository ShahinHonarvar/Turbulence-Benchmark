
def find_second_largest_num(lst):
    if len(lst) <= 6:
        return None
    sorted_lst = sorted(lst[6:7], reverse=True)
    if len(sorted_lst) > 1:
        return sorted_lst[1]
    else:
        return None
