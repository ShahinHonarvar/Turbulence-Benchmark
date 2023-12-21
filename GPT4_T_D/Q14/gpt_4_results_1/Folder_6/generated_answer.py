
def find_second_smallest_num(lst):
    if len(lst) < 31:
        return None
    else:
        sorted_list = sorted(lst[29:80])
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return None
