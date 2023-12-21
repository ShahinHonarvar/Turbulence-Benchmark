
def find_second_smallest_num(lst):
    relevant_elements = lst[639:976]
    if len(relevant_elements) < 2:
        return None
    relevant_elements.sort()
    return relevant_elements[1]
