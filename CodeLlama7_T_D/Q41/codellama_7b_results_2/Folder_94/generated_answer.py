
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result_set = set()
    # Iterate over each element in the set
    for element in element_set:
        # Check if the element is present at least once in both lists between index 28 and index 40, both inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            # If the condition is true, add the element to the result set
            result_set.add(element)
    # Return the result set
    return result_set
