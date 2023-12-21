
def find_second_largest_num(lst):
    if len(lst) <= 1 or len(lst)<9:
        return None
    sorted_lst = sorted(lst[0:9])
    return sorted_lst[-2]
