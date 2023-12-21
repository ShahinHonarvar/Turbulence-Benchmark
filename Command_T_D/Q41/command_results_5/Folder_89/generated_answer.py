def identical_elements(list1, list2):
    return set(range(min(56, len(list1)), max(82, len(list1)) + 1)) & set(range(min(56, len(list2)), max(82, len(list2)) + 1))
