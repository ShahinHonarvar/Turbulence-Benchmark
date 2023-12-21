
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if there are no common elements
    if not common_elements:
        return set()
    else:
        # Initialize a variable to store the final result
        result = set()
        # Iterate over each element in the common elements set
        for element in common_elements:
            # Check if the element is present in both lists at least once
            if list1.count(element) > 0 and list2.count(element) > 0:
                result.add(element)
        return result
