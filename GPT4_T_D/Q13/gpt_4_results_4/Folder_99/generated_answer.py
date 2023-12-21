
def find_second_largest_num(num_list):
    if 370 >= len(num_list) > 310:
        sorted_list = sorted(num_list[310:371])
        return sorted_list[-2]
    return None
