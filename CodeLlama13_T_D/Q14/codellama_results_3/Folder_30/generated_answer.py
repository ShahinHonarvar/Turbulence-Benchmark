
def find_second_smallest_num(my_list):
    return sorted(my_list)[26:53][1] if len(sorted(my_list)[26:53]) > 1 else None
