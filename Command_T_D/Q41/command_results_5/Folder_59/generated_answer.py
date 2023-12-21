def identical_elements(list1, list2):
    return set(range(min(x, y) for x, y in zip(list1, list2)))
