
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the nth smallest number
    nth_smallest_index = (len(my_list) // 2) - 1
    # Return the nth smallest number
    return my_list[nth_smallest_index]
