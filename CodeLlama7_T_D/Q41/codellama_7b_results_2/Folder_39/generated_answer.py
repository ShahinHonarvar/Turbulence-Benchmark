
def identical_elements(list1, list2):
    # Check if the lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store the identical elements
    identical_set = set()

    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element occurs in both lists between indices 20 and 30
        if list1[i] in list2[20:30] and list2[i] in list1[20:30]:
            # If it does, add it to the set of identical elements
            identical_set.add(list1[i])

    # Return the set of identical elements
    return identical_set
