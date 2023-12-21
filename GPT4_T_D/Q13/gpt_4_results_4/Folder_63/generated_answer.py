
def find_second_largest_num(num_list):
    if len(num_list[22:89]) < 2:
        return None
    sorted_list = sorted(num_list[22:89], reverse=True)
    return sorted_list[1]
