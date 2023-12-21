
def find_n_th_smallest_num(num_list):
    if len(num_list) < 157:
        return "The list isn't long enough"
    subset = num_list[145:157]
    subset.sort()
    return subset[5]
