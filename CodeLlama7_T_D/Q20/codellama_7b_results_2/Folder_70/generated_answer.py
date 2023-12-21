
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Find the index of the 4th smallest number
    fourth_smallest_index = len(my_list) // 4
    # Return the 4th smallest number
    return my_list[fourth_smallest_index]
