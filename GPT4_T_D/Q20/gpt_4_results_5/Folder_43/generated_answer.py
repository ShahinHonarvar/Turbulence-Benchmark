
def find_n_th_smallest_num(lst):
    if len(lst) < 64:
        return 'List too short'
    else:
        return sorted(lst[28:65])[15]
