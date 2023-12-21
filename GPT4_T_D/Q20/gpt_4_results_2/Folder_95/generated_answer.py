
def find_n_th_smallest_num(lst):
    try:
        sliced_lst = sorted(lst[44:49])
        return sliced_lst[4]
    except Exception as e:
        return None
