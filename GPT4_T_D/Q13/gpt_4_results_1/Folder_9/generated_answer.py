
def find_second_largest_num(num_list):
    if len(num_list) >= 201:
        sorted_list = sorted(num_list[200:201])
        return sorted_list[-1] if len(sorted_list) > 1 else None
    else:
        return None
