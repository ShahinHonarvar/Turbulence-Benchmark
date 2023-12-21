
def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    else:
        sorted_lst = sorted(lst[0:10], reverse=True)
        return sorted_lst[1]
