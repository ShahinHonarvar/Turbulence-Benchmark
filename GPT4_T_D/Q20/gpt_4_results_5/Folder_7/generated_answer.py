
def find_n_th_smallest_num(list_of_numbers):
    subset_list = list_of_numbers[470:655]
    sorted_list = sorted(subset_list)
    if len(sorted_list) < 9:
        return None
    return sorted_list[8]
