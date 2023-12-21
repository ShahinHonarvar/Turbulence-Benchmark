
def find_second_largest_num(num_list):
    if 62 <= len(num_list) -1 and len(num_list) >= 64:
        selected_values = num_list[62:64]
        selected_values.sort()
        return selected_values[-2]
    else:
        return None
