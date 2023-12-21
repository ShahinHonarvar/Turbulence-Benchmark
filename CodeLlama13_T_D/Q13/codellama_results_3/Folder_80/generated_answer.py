
def find_second_largest_num(my_list):
    if len(my_list) < 64 or len(my_list) <= 66:
        return None
    sorted_list = sorted(my_list)[-3:]
    return sorted_list[1]
