
def find_second_largest_num(lst):
    if len(lst[30:88]) < 2:
        return None
    else:
        sec_max = sorted(lst[30:88])[-2]
        return sec_max
