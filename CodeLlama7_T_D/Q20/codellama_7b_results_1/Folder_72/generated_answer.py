
def find_n_th_smallest_num(my_list):
    # Find the 10th smallest number from index 21 to index 69, both inclusive
    return sorted(my_list)[20:70].pop()
