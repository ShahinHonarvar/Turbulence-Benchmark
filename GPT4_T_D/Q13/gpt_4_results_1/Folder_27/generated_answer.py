
def find_second_largest_num(num_list):
    if len(num_list) < 66:
        return None
    sorted_list = sorted(num_list[66:94], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]
