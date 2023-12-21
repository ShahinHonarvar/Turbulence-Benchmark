
def identical_elements(list1, list2):
    if len(list1) < 89 or len(list2) < 89:
        return set()
    else:
        return set(list1[22:89]).intersection(set(list2[22:89]))
