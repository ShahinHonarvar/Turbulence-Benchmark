
def find_second_largest_num(lst):
    sublist = lst[80:201]
    if len(sublist) >= 2:
        sorted_list = sorted(sublist)
        return sorted_list[-2]
    else:
        return None
