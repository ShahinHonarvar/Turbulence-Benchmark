
def find_second_largest_num(lst):
    if len(lst) < 7:
        return None
    else:
        sub_lst = sorted(lst[6:7], reverse=True)   
        if len(sub_lst) < 2:
            return None
        else:
            return sub_lst[1]
