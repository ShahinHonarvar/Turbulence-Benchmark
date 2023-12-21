
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Check if any element occurs at least once in both lists anywhere between index 62 and index 78, both inclusive
    for i in range(62, 79):
        if list1[i] in common_elements and list2[i] in common_elements:
            return {list1[i], list2[i]}
    # If no such elements exist in the given lists, return an empty set
    return set()
