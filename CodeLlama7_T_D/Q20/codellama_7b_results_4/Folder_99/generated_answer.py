
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Return the 7th smallest number from index 391 to index 414, both inclusive
    return my_list[391:414 + 1].index(my_list[391]) + 391
