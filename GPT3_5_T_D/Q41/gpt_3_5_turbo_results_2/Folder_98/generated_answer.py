
def identical_elements(list1, list2):
    # Create a set to store the identical elements
    identical = set()
    # Iterate through the elements of the first list
    for element1 in list1[:6]:
        # Check if the element is also in the second list
        if element1 in list2[:6]:
            # If it is, add it to the set
            identical.add(element1)
    # Return the set of identical elements
    return identical
