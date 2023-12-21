
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set of all elements in list1
    set1 = set(list1)

    # Create a set of all elements in list2
    set2 = set(list2)

    # Return the intersection of both sets
    return set1 & set2
