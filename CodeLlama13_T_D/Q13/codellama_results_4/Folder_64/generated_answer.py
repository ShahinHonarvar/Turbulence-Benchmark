
def find_second_largest_num(my_list):
    if len(my_list) < 2:
        return None

    sorted_list = sorted(my_list)[-5:-1]
    return sorted_list[1]
