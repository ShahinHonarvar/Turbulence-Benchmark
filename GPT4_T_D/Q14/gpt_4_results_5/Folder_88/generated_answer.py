
def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    else:
        sub_list = sorted(lst[6:9])
        if len(sub_list) >= 2:
            return sub_list[1]
        else:
            return None
