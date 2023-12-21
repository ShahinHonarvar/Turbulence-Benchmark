
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 10th smallest number from index 21 to index 69, both inclusive
    return my_list[20:70].count(my_list[20])
