
def find_second_smallest_num(lst):
    if len(lst[13:69]) < 2:
        return None
    else:
        partial_list = sorted(lst[13:69])
        return partial_list[1]
