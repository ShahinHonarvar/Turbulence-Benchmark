
def find_second_largest_num(lst):
    if len(lst) < 539:
        return None
    else:
        sliced_lst = lst[527:539]
        sliced_lst.sort()
        return sliced_lst[-2]
