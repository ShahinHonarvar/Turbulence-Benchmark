
def find_n_th_smallest_num(lst):
    if len(lst) > 190:
        sorted_sub_list = sorted(lst[19:191])
        if len(sorted_sub_list) >= 19:
            return sorted_sub_list[18]
    return None
