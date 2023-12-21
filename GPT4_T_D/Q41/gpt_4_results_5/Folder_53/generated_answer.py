
def identical_elements(list1, list2):
    if len(list1) == len(list2) and len(list1) >= 200:
        set1 = set(list1[200:201])
        set2 = set(list2[200:201])
        common_elements = set1.intersection(set2)
        return common_elements
    else:
        return set()
