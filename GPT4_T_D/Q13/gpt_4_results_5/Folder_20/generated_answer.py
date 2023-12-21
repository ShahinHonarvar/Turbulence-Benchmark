
def find_second_largest_num(lst):
    try:
        sub_lst = lst[56:67]
        return sorted(sub_lst, reverse=True)[1]
    except IndexError:
        return None
