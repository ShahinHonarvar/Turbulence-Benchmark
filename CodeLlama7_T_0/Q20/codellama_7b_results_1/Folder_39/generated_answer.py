
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 7th smallest number from index 47 to index 89, both inclusive
    return my_list[47:89+1].index(my_list[47:89+1][-1]) + 47
