
def find_second_smallest_num(num_list):
    if len(num_list) < 38:
        return None
    else:
        sorted_list = sorted(num_list[37:77])
        return sorted_list[1] if len(sorted_list) > 1 else None
