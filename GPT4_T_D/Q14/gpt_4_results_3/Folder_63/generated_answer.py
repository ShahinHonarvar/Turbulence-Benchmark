
def find_second_smallest_num(num_list):
    if len(num_list) < 83:
        return None
    sorted_num_list = sorted(num_list[56:83])
    if len(sorted_num_list) < 2:
        return None
    return sorted_num_list[1]
