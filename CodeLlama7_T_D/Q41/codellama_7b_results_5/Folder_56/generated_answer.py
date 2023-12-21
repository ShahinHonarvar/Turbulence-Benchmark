
def identical_elements(list1, list2):
    # Check if both lists are of the same size and have at least one element
    if len(list1) != len(list2) or len(list1) == 0:
        return set()
    # Initialize an empty set to store the identical elements
    identical_elements = set()
    # Iterate through both lists simultaneously
    for i in range(len(list1)):
        # Check if the current element is present in both lists at index 1 and index 8
        if list1[i] in list2[1:9+1] and list2[i] in list1[1:9+1]:
            identical_elements.add(list1[i])
    # Return the set of identical elements
    return identical_elements
