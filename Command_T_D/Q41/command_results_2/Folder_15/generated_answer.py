def identical_elements(list1, list2):
    result = set(list1[2:]).intersection(list2[2:])
    return result
