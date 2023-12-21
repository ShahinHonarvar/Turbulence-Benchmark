
def find_n_th_smallest_num(num_list):
    num_list.sort()
    if len(num_list) >= 17:
        return num_list[16]
    else:
        return "List does not contain 17 elements"
