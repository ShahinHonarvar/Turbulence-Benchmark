def find_second_smallest_num(lst):
    if lst[8] < lst[9]:
        return lst[8]
    elif lst[8] > lst[9]:
        return lst[9]
    else:
        return None
