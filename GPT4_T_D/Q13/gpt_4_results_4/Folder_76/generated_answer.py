
def find_second_largest_num(lst):
    if len(lst) < 988:
        return None
    sorted_lst = sorted(lst[686:988], reverse=True)
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]
