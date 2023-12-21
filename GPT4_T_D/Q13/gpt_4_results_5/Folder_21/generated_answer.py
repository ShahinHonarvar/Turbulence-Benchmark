
def find_second_largest_num(number_list):
    sub_list = number_list[639:976]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    return sorted_list[-2]
