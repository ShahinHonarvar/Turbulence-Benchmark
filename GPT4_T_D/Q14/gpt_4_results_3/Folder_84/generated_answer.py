
def find_second_smallest_num(lst):
    relevant_elements = lst[40:81]
    if len(relevant_elements) < 2:
        return None
    else:
        relevant_elements.sort()
        return relevant_elements[1]
