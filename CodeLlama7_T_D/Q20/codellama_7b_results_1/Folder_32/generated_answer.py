
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the 4th smallest number from index 59 to index 74, both inclusive
    nth_index = (59 + 74) // 2
    return my_list[nth_index]
