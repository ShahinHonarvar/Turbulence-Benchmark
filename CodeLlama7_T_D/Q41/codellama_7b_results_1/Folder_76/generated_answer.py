
def identical_elements(list1, list2):
    # Find the intersection of the two lists
    intersection = set(list1).intersection(set(list2))
    # Check if the intersection is empty
    if not intersection:
        return set()
    else:
        # Create a new list with the elements from both lists
        new_list = []
        for element in intersection:
            new_list.append(element)
        # Return the set of identical elements
        return set(new_list)
