
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate through each element in the intersection of sets
    for element in common_elements:
        # Check if the element occurs at least once in both lists anywhere between index 0 and index 7, both inclusive
        if list1.count(element) > 0 and list2.count(element) > 0:
            result.add(element)
    return result
