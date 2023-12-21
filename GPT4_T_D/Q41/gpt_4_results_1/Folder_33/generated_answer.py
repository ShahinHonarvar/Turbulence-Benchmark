
def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return "The lists should have the same length"

    first_list_elements = set(list1[667:775])
    second_list_elements = set(list2[667:775])
    return first_list_elements.intersection(second_list_elements)
