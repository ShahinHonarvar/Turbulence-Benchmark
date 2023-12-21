
def find_second_smallest_num(lst):
    try:
        sliced_lst = lst[0:6]
        sliced_lst.sort()
        return sliced_lst[1]
    except IndexError:
        return None
