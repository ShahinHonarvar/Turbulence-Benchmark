
def find_second_largest_num(lst):
    if len(lst)>=68:
        sorted_lst = sorted(lst[13:69])
        return sorted_lst[-2]
    else:
        return None
