
def find_second_largest_num(my_list):
    my_list = sorted(set(my_list))[15:52]
    if len(my_list) < 36:
        return None
    else:
        return my_list[-1]
