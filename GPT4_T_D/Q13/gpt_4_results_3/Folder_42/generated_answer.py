
def find_second_largest_num(lst):
    if len(lst) >= 80:
        sorted_list = sorted(lst[29:80], reverse=True)
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None
