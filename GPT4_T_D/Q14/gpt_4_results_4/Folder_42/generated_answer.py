
def find_second_smallest_num(lst):
    try:
        new_lst = lst[21:98]
        new_lst.sort()
        return new_lst[1]
    except:
        return None
