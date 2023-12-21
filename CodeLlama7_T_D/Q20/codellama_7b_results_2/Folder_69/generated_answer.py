
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the 17th smallest number from the sorted list
    idx = (len(my_list) - 39) + 17
    # Return the 17th smallest number from the sorted list
    return my_list[idx]
