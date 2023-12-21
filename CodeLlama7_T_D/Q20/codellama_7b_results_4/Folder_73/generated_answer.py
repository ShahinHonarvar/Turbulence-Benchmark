
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # return the nth smallest number from index 35 to index 60, both inclusive
    return my_list[34:61].index(my_list[34:61]) + 35
