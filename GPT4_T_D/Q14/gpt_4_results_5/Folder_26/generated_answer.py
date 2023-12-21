
def find_second_smallest_num(lst):
    sub_lst = lst[62:79]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]
