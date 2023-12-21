
def find_n_th_smallest_num(lst):
    if len(lst[43:81]) >= 6:
        return sorted(lst[43:81])[5]
    else:
        return None
