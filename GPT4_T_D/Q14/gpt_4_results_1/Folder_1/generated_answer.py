
def find_second_smallest_num(num_list):
    if len(num_list[34:56]) >= 2:
        sorted_list = sorted(num_list[34:56])
        return sorted_list[1]
    else:
        return None
