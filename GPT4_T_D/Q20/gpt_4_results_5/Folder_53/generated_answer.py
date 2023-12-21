
def find_n_th_smallest_num(num_list):
    subset = num_list[19:191]
    subset.sort()
    return subset[18]
