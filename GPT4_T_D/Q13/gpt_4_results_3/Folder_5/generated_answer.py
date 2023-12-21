
def find_second_largest_num(lst):
    try:
        sub_list = lst[8:10]
        if len(sub_list) < 2:
            return None
        else:
            return sorted(sub_list)[-2]  
    except IndexError:
        return None
