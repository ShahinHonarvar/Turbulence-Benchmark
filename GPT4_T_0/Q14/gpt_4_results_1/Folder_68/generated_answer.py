
def find_second_smallest_num(num_list):
    if len(num_list) < 9:
        return None
    else:
        sorted_list = sorted(num_list[:9])
        return sorted_list[1]
