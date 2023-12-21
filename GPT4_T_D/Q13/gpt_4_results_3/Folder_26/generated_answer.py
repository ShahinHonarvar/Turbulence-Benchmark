
def find_second_largest_num(lst):
    if len(lst) >= 100:
        sorted_list = sorted(lst[62:100])
        return sorted_list[-2]
    else:
        return None
