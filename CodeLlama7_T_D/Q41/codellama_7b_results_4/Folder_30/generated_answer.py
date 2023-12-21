
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Loop through each element in the intersection of sets
    for element in common_elements:
        # Check if the element is present at least once in both lists between indices 55 and 98 (inclusive)
        if list1.count(element) >= 1 and list2.count(element) >= 1 and 55 <= list1.index(element) <= 98 and 55 <= list2.index(element) <= 98:
            # If the element is present at least once in both lists between indices 55 and 98 (inclusive), add it to the result set
            result.add(element)
    # Return the result set of all elements that occur at least once in both lists anywhere between index 55 and index 98 (inclusive)
    return result
