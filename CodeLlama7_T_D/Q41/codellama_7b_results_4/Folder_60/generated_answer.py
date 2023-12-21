
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists
    for i in range(75, 86):
        # Check if the current element in both lists is the same
        if list1[i] == list2[i]:
            # Add the element to the set of identical elements
            identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements
