
def find_second_largest_num(lst):
    if len(lst)>=750:
        sub_list = lst[246:751]
        sub_list.sort()
        if len(sub_list)>1:
            return sub_list[-2]
        else:
            return None
    else:
        return None
