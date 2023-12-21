
def find_second_largest_num(lst):
    if len(lst) < 200:
        return None
    else:
        sliced_lst = lst[100:201]
        sliced_lst.sort()
        return sliced_lst[-2]
