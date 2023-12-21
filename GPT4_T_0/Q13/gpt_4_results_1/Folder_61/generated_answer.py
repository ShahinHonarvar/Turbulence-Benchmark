
def find_second_largest_num(num_list):
    if len(num_list) < 8:
        return None
    else:
        sorted_list = sorted(num_list[:8], reverse=True)
        return sorted_list[1]
