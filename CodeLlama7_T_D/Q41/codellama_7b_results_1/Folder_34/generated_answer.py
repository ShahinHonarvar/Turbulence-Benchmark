
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the desired elements
    desired_elements = set()
    # Iterate over the common elements and check if they occur at least once in both lists anywhere between index 60 and index 200, both inclusive
    for element in common_elements:
        # Check if the element occurs at least once in list1 within the specified range
        if list1.count(element) >= 1 and list1.index(element) >= 60 and list1.index(element) <= 200:
            # If it does, check if it also occurs at least once in list2 within the specified range
            if list2.count(element) >= 1 and list2.index(element) >= 60 and list2.index(element) <= 200:
                # If it does, add the element to the desired elements set
                desired_elements.add(element)
    return desired_elements
