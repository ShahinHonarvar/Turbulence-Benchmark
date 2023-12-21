
def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    else:
        return sorted(lst[0:10])[-2]
