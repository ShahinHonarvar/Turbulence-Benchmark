
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate through each element in the intersection of sets
    for element in common_elements:
        # Check if the element is present at least once in both lists between indices 4 and 8, inclusive
        if list1.count(element) > 0 and list2.count(element) > 0 and (list1.index(element) >= 4 and list1.index(element) <= 8) or (list2.index(element) >= 4 and list2.index(element) <= 8)):
            # If the element is present in both lists between indices 4 and 8, inclusive, add it to the result set
            result.add(element)
    return result
