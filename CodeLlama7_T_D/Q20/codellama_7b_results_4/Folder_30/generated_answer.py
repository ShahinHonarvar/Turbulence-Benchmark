
def find_n_th_smallest_num(my_list):
    # Find the 19th smallest number from index 78 to index 99, both inclusive
    return sorted(my_list)[78:99].index(sorted(my_list)[78:99])+78
