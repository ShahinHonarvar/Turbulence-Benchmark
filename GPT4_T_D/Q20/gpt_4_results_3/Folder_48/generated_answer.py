
def find_n_th_smallest_num(num_list):
    sliced_list = num_list[127:849]
    sorted_list = sorted(sliced_list)
    return sorted_list[9]
