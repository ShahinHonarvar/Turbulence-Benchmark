
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over each element in the intersection of sets
    for element in common_elements:
        # Check if the element occurs at least once in both lists between indices 1 and 5, inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and list1.index(element) <= 5 and list2.index(element) <= 5:
            # If the element occurs at least once in both lists between indices 1 and 5, inclusive, add it to the result set
            result.add(element)
    # Return the result set
    return result
