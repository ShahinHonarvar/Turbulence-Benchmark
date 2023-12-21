
def find_second_largest_num(my_list):
    if len(my_list) < 64:
        return None
    sorted_list = sorted(my_list, reverse=True)
    return sorted_list[63]
