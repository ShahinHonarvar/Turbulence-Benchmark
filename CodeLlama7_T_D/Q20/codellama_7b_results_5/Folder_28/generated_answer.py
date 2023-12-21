
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 12th smallest number from index 58 to index 93, both inclusive
    return my_list[58:94].index(12)
