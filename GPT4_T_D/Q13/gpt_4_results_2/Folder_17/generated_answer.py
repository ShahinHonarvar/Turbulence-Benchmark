
def find_second_largest_num(lst):
    if 62 <= len(lst) <= 78:
        sub_lst = lst[62:79]
        sub_lst.remove(max(sub_lst))
        if len(sub_lst) > 0:
            return max(sub_lst)
    return None
