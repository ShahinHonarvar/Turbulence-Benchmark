
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 12th smallest number from index 20 to index 62, both inclusive
    return my_list[19:63].index(my_list[19:63][-12])
