
def identical_elements(list1, list2):
    # Initialize an empty set to store the identical elements
    identical_elements = set()

    # Iterate over both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element is also present in the other list
        if list1[i] in list2 and list2[i] in list1:
            # Add the identical element to the set
            identical_elements.add((list1[i], list2[i])))

    return identical_elements
