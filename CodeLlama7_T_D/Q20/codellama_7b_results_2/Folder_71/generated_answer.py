
def find_n_th_smallest_num(my_list):
    # Sort the list in ascending order
    my_list.sort()
    # Get the index of the 4th smallest number from index 56 to index 70, both inclusive
    nth_index = (56 + 70) // 2
    return my_list[nth_index]
