
def identical_elements(list1, list2):
    # Check that both lists are of the same size
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same size")
    # Create a set to store the identical elements
    identical_set = set()
    # Loop through the lists and check for identical elements between index 639 and index 975
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set
