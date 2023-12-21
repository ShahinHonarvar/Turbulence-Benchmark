
def find_second_smallest_num(num_list):
    selected_elements = num_list[28:33]
    if len(selected_elements) < 2:
        return None
    else:
        selected_elements.sort()
        return selected_elements[1]
