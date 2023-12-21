
def find_second_smallest_num(my_list):
    return sorted(my_list)[28:33][1] if len(sorted(my_list)[28:33]) > 1 else None
