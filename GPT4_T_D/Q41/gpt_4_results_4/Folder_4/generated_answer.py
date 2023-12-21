
def identical_elements(list1, list2):
    list1_subset = list1[12:93]
    list2_subset = list2[12:93]
    intersecting_elements = set(list1_subset).intersection(set(list2_subset))
    return intersecting_elements
