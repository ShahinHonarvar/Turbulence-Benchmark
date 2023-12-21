
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 9th smallest number from index 106 to index 254, both inclusive
    return my_list[106:254+1].index(my_list[106:254+1][-1]) + 106
