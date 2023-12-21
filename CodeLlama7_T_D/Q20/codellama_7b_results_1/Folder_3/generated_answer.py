
def find_n_th_smallest_num(my_list):
    # Find the 14th smallest number from index 24 to index 37, both inclusive
    return sorted(my_list)[23:38].sort()[13]
