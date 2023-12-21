
def find_second_smallest_num(lst):
    if len(lst) < 9:
        return None
    else:
        sorted_list = sorted(lst[:9])
        return sorted_list[1]
