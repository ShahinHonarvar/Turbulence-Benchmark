
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate through each element in the intersection of both lists
    for element in common_elements:
        # If the element is found at least once in both lists between indices 17 and 78, inclusive, add it to the result set
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 17 and list1.index(element) <= 78) or (list2.index(element) >= 17 and list2.index(element) <= 78)):
            result.add(element)
    # Return the set of identical elements found between indices 17 and 78, inclusive
    return result
