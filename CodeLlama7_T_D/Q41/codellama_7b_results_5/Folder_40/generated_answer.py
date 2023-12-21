
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if no common elements are found
    if not common_elements:
        return set()

    # Initialize a dictionary to store the indices of each element in both lists
    indices = {}

    # Iterate through both lists and update the indices of each element
    for i, elem in enumerate(list1):
        if elem in indices:
            indices[elem].append(i)
        else:
            indices[elem] = [i]

    for i, elem in enumerate(list2):
        if elem in indices:
            indices[elem].append(i)
        else:
            indices[elem] = [i]

    # Return the set of all elements that occur at least once in both lists anywhere between index 0 and index 1, both inclusive
    return {elem for elem in common_elements if any(idx in range(len(list1))) for idx in indices[elem]}}```
