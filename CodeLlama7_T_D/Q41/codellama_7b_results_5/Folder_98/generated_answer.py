
def identical_elements(list1, list2):
    # Create a set of all elements in list1 and list2
    set1 = set(list1) | set(list2)
    # Create an empty set to store the identical elements
    identical_elements = set()

    # Loop through each element in set1
    for element in set1:
        # Check if the element is in both list1 and list2
        if element in list1 and element in list2:
            # If the element is in both lists, add it to the identical_elements set
            identical_elements.add(element)

    return identical_elements
