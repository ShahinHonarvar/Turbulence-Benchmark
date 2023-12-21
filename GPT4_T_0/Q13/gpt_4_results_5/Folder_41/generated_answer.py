
def find_second_largest_num(num_list):
    if len(num_list) < 7:
        return None
    else:
        return sorted(num_list[6:7])[-2] if len(num_list[6:7]) > 1 else None
