
def identical_elements(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    # Initialize an empty set to store the identical elements
    identical_set = set()
    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # If the current element of list1 is in list2, add it to the set of identical elements
        if list1[i] in list2:
            identical_set.add(list1[i])
    # Return the set of identical elements
    return identical_set
