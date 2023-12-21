
def find_n_th_smallest_num(my_list, n):
    # Sort the list in ascending order
    my_list.sort()
    # Return the n-th smallest number
    return my_list[n - 1]
