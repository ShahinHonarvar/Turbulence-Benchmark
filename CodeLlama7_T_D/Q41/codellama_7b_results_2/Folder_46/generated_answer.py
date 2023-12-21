
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    matching_elements = set()

    # Iterate over the common elements and check if they appear at least once in both lists between index 30 and index 87
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        if count1 >= 30 and count1 <= 87 and count2 >= 30 and count2 <= 87:
            matching_elements.add(element)

    # Return the set of matching elements
    return matching_elements
