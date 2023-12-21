
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 8 and index 9, both inclusive
    for element in common_elements:
        # If the element occurs at least once in both lists between index 8 and index 9, both inclusive, add it to the result set
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 8 and list1.index(element) <= 9) or (list2.index(element) >= 8 and list2.index(element) <= 9)):
            result.add(element)
    # Return the set of all elements that occur at least once in both lists between index 8 and index 9, both inclusive
    return result
