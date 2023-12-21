def identical_elements(list1, list2):
    return set(range(len(list1), min(len(list1), len(list2)) + 1, -1))
