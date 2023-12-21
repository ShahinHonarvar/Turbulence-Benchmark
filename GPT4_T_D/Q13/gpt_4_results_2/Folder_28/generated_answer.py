
def find_second_largest_num(lst):
    if len(lst) < 64:
        return None
    else:
        selected_list = lst[62:64]
        selected_list.sort()
        return selected_list[0]
