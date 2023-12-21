
def find_second_smallest_num(num_list):
    sorted_list = sorted(num_list[:6])
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
