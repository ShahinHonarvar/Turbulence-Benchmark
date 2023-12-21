
def find_n_th_smallest_num(num_list):
    sorted_list = sorted(num_list)
    if len(sorted_list) < 11:
        return None
    return sorted_list[10]
