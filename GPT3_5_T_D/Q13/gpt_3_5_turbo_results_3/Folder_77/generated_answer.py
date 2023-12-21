
def find_second_largest_num(lst):
    sub_lst = lst[527:539]
    sorted_lst = sorted(sub_lst, reverse=True)
    return sorted_lst[1] if len(sorted_lst) > 1 else None
