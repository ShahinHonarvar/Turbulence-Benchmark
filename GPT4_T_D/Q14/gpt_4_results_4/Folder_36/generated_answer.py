
def find_second_smallest_num(lst):
    if len(lst) >= 557:
        sorted_list = sorted(lst[209:557])
        return sorted_list[1] if len(sorted_list) > 1 else None
    return None
