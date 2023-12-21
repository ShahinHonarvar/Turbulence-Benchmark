
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate over each element in the intersection of sets
    for element in common_elements:
        # Check if the element is present at least once in both lists
        if list1.count(element) > 0 and list2.count(element) > 0:
            # If it is, add it to the result set
            result.add(element)
    return result
