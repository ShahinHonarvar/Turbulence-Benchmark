
def find_second_smallest_num(num_list):
    selected_list = num_list[661:925]
    sorted_list = sorted(selected_list)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
