
def find_second_smallest_num(lst):
    sublist = lst[35:50]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    else:
        return sorted_sublist[1]
