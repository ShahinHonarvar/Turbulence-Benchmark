
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Return an empty set if there are no identical elements
    if not intersection:
        return set()

    # Initialize a variable to keep track of the indices where the identical elements appear
    indices = []

    for element in intersection:

        # Find the indices where the identical element appears in both lists
        index1 = list1.index(element)
        index2 = list2.index(element)

        # If the identical element appears in both lists at least once, add its indices to the set of indices
        if index1 != -1 and index2 != -1:
            indices.append((index1, index2))

    # Return the set of indices where the identical elements appear in both lists
    return set(indices)
