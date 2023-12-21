def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(range(59, 97)) & set(list1) & set(list2)
