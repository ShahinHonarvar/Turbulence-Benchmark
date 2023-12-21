
def find_second_smallest_num(num_list):
    between_indexes = num_list[26:53]
    if len(between_indexes) < 2:
        return None
    else:
        return sorted(between_indexes)[1]
