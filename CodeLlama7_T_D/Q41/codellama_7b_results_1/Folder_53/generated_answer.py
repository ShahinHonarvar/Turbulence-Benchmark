
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result_set = set()
    # Loop through each element in the common elements set
    for element in common_elements:
        # Check if the element is present at least once in both lists between indices 200 and 200 (inclusive)
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            # If it is, add it to the result set
            result_set.add(element)
    # Return the result set
    return result_set
