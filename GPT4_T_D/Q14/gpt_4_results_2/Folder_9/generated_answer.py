
def find_second_smallest_num(lst):
    lst = lst[70:201]

    if len(lst) < 2:
        return None
    else:
        lst.sort()
        return lst[1]
