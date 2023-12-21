
def find_n_th_smallest_num(lst):
    sorted_list = sorted(lst[40:76])
    if len(sorted_list) >= 19:
        return sorted_list[18]
    else:
        return 'Not enough elements in the list'
