
def find_second_largest_num(num_list):
    if 21 <= len(num_list) <= 97:
        sorted_list = sorted(num_list[21:98], reverse=True)
        if len(sorted_list) > 1:
            return sorted_list[1]
    return None
