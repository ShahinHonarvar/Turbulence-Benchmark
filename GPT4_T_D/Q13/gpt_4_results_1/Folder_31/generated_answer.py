
def find_second_largest_num(num_list):
    if len(num_list)>=89:
        subset_list = num_list[75:89]
        subset_list.sort(reverse=True)
        if len(subset_list)>1:
            return subset_list[1]
    return None
