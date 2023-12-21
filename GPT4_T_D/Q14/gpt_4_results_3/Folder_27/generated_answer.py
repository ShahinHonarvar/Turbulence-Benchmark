
def find_second_smallest_num(num_list):
    if len(num_list[25:60]) < 2:
        return None
    sorted_list = sorted(num_list[25:60])
    return sorted_list[1]
