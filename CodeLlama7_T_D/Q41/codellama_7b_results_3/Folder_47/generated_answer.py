
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result_set = set()
    # Iterate through each element in the intersection of both sets
    for element in common_elements:
        # Check if the element is present at least once in both lists between index 37 and 76 (both inclusive)
        if list1.count(element) >= 37 and list2.count(element) >= 37 and \
                                           list1.index(element) <= 76 and list2.index(element) <= 76:
            # If the element is present at least once in both lists between index 37 and 76 (both inclusive), add it to the result set
            result_set.add(element)
    # Return the set of all elements that occur at least once in both lists anywhere between index 37 and index 76 (both inclusive)
    return result_set
