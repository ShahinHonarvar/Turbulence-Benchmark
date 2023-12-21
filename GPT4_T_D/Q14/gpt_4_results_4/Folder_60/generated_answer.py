
def find_second_smallest_num(num_list):
    if len(num_list) < 99:
        return None
    else:
        selected_list = num_list[56:99]
        selected_list.sort()
        return selected_list[1] if len(selected_list) > 1 else None
