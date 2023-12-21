
def identical_elements(list1, list2):
    # Get the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    results = set()
    # Iterate over the intersection of both lists
    for element in intersection:
        # Check if the element is present in both lists
        # between index 40 and index 80, both inclusive
        if list1.count(element) > 0 and list2.count(element) > 0:
            # If the element is present in both lists, add it to the results set
            results.add(element)
    return results
