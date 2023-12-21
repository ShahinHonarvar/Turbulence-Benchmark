
def find_second_largest_num(my_list):
    return sorted(my_list)[29:52][-1] if len(sorted(my_list)) > 40 else None
