
def find_second_largest_num(num_list):
    if len(num_list) >= 69:
        sorted_list = sorted(num_list[13:69], reverse=True)
        if len(sorted_list) >= 2:
            return sorted_list[1]
    return None
