
def find_second_largest_num(lst):
    if len(lst) < 81:
        return None
    else:
        sub_list = lst[40:81]
        sub_list.sort()
        return sub_list[-2]
