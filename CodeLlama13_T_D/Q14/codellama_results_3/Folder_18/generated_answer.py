
def find_second_smallest_num(my_list):
    my_list = sorted(set(my_list))[29:30]
    if len(my_list) == 0:
        return None
    else:
        return my_list[0]
