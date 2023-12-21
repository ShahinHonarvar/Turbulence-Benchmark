
def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    else:
        sorted_list = sorted(lst[0:10])
        return sorted_list[-2]
