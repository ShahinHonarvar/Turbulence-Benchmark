
def find_second_smallest_num(num_list):
    if len(num_list) < 988:
        return None
    else:
        sorted_list = sorted(num_list[686:988])
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
