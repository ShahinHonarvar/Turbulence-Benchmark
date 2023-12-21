
def identical_elements(list1, list2):
    # Find the intersection of both lists
    intersection = set(list1).intersection(set(list2))
    # Check if there are any elements in common between the two lists
    if len(intersection) > 0:
        # Initialize an empty set to store the identical elements
        identical_elements = set()
        # Loop through each element in the intersection
        for element in intersection:
            # Check if the element is present in both lists at least once between index 40 and index 80, both inclusive
            if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) <= 80 and list1.index(element) >= 40) or (list2.index(element) <= 80 and list2.index(element) >= 40)):
                # If the element is present in both lists at least once between index 40 and index 80, both inclusive, add it to the set of identical elements
                identical_elements.add(element)
        return identical_elements
    else:
        # If there are no elements in common between the two lists, return an empty set
        return set()
