
def find_n_th_smallest_num(my_list):
    # sort the list in ascending order
    my_list.sort()
    # return the 6th smallest number from index 50 to index 81, both inclusive
    return my_list[50:82].count(my_list[50:82])
