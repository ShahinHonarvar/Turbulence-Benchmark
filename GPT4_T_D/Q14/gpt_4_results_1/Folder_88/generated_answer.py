
def find_second_smallest_num(num_list):
    if len(num_list) < 9:
        return None
    else:
        selected_elements = num_list[6:9]
        selected_elements.sort()
        if len(selected_elements) > 1:
            return selected_elements[1]
        else:
            return None
