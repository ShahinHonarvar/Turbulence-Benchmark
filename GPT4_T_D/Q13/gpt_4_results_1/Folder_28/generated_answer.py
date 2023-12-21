
def find_second_largest_num(lst):
    if len(lst) >= 64:
        sorted_list = sorted(lst[62:64])
        return sorted_list[-2]
    return None
