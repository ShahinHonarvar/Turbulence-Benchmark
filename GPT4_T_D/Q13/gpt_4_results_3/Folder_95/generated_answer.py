
def find_second_largest_num(lst):
    sub_list = lst[82:87]
    
    if len(sub_list) < 2:
        return None

    sub_list.sort()

    return sub_list[-2]
