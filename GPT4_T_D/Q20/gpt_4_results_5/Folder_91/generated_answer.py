
def find_n_th_smallest_num(num_list):
    num_list.sort()
    if len(num_list)>=8:
        return num_list[7]
    else:
        return "Size of the list is less than 8"
