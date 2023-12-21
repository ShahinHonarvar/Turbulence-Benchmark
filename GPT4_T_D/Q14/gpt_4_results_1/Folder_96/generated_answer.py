
def find_second_smallest_num(lst):
    if len(lst) < 51:
        return None
    else:
        selected_elements = lst[50:201]
        selected_elements.sort()
        if len(selected_elements) < 2:
            return None
        else:
            return selected_elements[1]
