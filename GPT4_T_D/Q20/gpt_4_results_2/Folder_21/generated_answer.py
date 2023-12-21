
def find_n_th_smallest_num(num_list):
    sublist = num_list[299:636]
    sublist.sort()
    return sublist[11]
