
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the n-th smallest number
    n_th_index = (len(my_list) - 1) * 0.5
    # Return the n-th smallest number
    return my_list[n_th_index]
