
def find_second_largest_num(num_list):
    if len(num_list) < 41:
        return None
    else:
        selected_elements = num_list[28:41]
        selected_elements.sort()
        return selected_elements[-2] if len(selected_elements) >= 2 else None
