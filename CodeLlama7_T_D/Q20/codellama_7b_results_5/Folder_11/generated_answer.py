
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 13th smallest number from index 54 to index 87, both inclusive
    return my_list[54:87+1].index(13)
