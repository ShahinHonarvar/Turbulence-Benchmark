
def identical_elements(list1, list2):
    elements = set(list1[:7]).intersection(set(list2[:7]))
    return elements
