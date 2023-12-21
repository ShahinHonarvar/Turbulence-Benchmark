
def find_second_largest_num(lst):
    if len(lst) < 52:
        return None
    sliced_lst = sorted(lst[15:52], reverse=True)
    if len(sliced_lst) < 2:
        return None
    return sliced_lst[1]
