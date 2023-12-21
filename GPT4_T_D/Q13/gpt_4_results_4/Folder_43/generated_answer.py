
def find_second_largest_num(lst):
    elements_range = lst[68:87]
    if len(elements_range)<2:
        return None
    else:
        elements_range.sort()
        return elements_range[-2]
