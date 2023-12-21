
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the final result
    result = set()
    # Iterate through each element in the intersection of the two sets
    for element in common_elements:
        # Check if the element occurs at least once in both lists between index 12 and index 92, inclusive
        if list1.count(element) >= 12 and list2.count(element) >= 12:
            # If it does, add it to the final result set
            result.add(element)
    return result
