
def identical_elements(list1, list2):
    # Check if the lists are empty or None
    if not list1 or not list2:
        return set()

    # Get the size of the lists
    n = len(list1)

    # Create a set to store the identical elements
    identical_elements = set()

    # Loop through each element in the first list
    for i in range(22, 88 + 1):
        # Check if the current element is in both lists
        if list1[i] in list2:
            # Add the element to the set of identical elements
            identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements
