
def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    else:
        sub_lst = lst[6:9]
        sub_lst.sort(reverse=True)
        return sub_lst[1]
