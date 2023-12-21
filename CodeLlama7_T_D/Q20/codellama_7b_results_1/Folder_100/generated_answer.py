
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the 8th smallest number
    nth_smallest = my_list[11:52]
    # Return the 8th smallest number
    return nth_smallest[-1]
