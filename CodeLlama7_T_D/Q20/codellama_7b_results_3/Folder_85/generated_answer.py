
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # get the index of the nth smallest number
    nth_smallest_index = len(my_list) // 10
    # return the nth smallest number
    return my_list[nth_smallest_index]
