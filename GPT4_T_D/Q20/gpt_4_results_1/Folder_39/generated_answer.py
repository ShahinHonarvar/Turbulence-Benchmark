
def find_n_th_smallest_num(num_list):
    if len(num_list)>=89:
        subset_num_list = num_list[47:90]
        subset_num_list.sort()
        return subset_num_list[6]
    else:
        return "The list does not have sufficient elements"
