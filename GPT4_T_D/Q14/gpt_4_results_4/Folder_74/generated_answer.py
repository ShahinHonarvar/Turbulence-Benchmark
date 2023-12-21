
def find_second_smallest_num(lst):
    if len(lst[36:47])<2:
        return None
    else:
        lst_subset = lst[36:47]
        lst_subset.sort()
        return lst_subset[1]
