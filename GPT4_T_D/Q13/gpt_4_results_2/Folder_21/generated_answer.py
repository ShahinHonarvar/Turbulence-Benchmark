
def find_second_largest_num(num_list):
    selected_list = num_list[639:976]
    if not selected_list:
        return None
    else:
        selected_list.sort()
        return selected_list[-2]
