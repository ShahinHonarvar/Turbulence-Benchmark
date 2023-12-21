
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 6th smallest number from index 50 to index 81, both inclusive
    return my_list[50:82].index(my_list[50:82]) + 50
