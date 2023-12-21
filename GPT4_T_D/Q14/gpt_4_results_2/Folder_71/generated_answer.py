
def find_second_smallest_num(lst):
    try:
        subset_list = lst[29:52]
        subset_list.sort()
        return subset_list[1]
    except IndexError:
        return None
