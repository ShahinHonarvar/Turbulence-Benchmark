
def find_second_smallest_num(num_list):
    if len(num_list) <= 1:
        return None
    else:
        sorted_list = sorted(num_list[:5])
        if len(sorted_list) == 1:
            return None
        else:
            return sorted_list[1]
