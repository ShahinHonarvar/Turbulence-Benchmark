
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate through each element in the intersection of sets
    for element in common_elements:
        # Check if the element is present at least once between index 62 and index 92, both inclusive
        if list1.index(element) >= 62 and list1.index(element) <= 92 or list2.index(element) >= 62 and list2.index(element) <= 92:
            # If the element is present at least once between index 62 and index 92, both inclusive, add it to the result set
            result.add(element)
    # Return the result set
    return result
