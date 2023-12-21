
def find_second_smallest_num(my_list):
    if len(my_list) <= 1:
        return None
    my_list = sorted(set(my_list))[16:79]
    if len(my_list) < 2:
        return None
    return my_list[1]
