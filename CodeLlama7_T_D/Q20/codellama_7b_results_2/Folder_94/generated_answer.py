
def find_n_th_smallest_num(my_list):
    # Find the 6th smallest number from index 57 to index 70, both inclusive
    return sorted(my_list)[57:70+1].index(min(sorted(my_list)[57:70+1]))
