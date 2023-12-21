
def find_second_largest_num(num_list):
    sorted_list = sorted(num_list[30:88], reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None
