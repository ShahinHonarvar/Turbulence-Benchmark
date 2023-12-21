
def identical_elements(list1, list2):
    # Get the intersection of the two lists
    intersection = list(set(list1).intersection(list2))
    # Initialize an empty set to store the results
    results = set()
    # Iterate over the intersection of the two lists
    for element in intersection:
        # Check if the element occurs at least once in both lists between index 50 and index 54, both inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 50 and list1.index(element) <= 54) or (list2.index(element) >= 50 and list2.index(element) <= 54)):
            # If the element occurs at least once in both lists between index 50 and index 54, both inclusive, add it to the results set
            results.add(element)
    # Return the set of identical elements found between index 50 and index 54, both inclusive
    return results
