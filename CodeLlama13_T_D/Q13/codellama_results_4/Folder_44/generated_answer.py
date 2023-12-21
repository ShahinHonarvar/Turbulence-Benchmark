
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)[13:69]
    if len(sorted_list) == 0:
        return None
    else:
        return sorted_list[-1]
