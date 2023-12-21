
def find_second_largest_num(my_list):
    my_list = list(set(my_list))
    if len(my_list) < 2:
        return None
    else:
        return sorted(my_list)[-2]
