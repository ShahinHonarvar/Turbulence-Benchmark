
def find_second_largest_num(lst):
    try:
        sub_lst = lst[37:77]
        sub_lst.sort()
        return sub_lst[-2]
    except:
        return None
