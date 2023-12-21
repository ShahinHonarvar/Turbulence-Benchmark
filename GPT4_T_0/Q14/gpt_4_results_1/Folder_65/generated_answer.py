
def find_second_smallest_num(num_list):
    if len(num_list) < 58:
        return None
    else:
        return sorted(num_list[56:58])[1] if len(num_list[56:58]) > 1 else None
