
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Find the index of the 10th smallest number
    nth_index = len(my_list) // 20 * 19
    # Return the 10th smallest number
    return my_list[nth_index]
