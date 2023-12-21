
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements between the two lists
    for element in common_elements:
        # Check if the element occurs at least once in both lists anywhere between index 33 and index 36, both inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (33 <= list1.index(element) <= 36 or 33 <= list2.index(element) <= 36)):
            # If the element occurs at least once in both lists anywhere between index 33 and index 36, both inclusive, add it to the result set
            result.add(element)
    return result
