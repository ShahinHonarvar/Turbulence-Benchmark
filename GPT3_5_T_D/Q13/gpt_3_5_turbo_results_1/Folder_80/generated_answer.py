
def find_second_largest_num(lst):
    selected_lst = lst[64:67]
    if len(selected_lst) < 2:
        return None
    selected_lst.sort()
    return selected_lst[-2]
