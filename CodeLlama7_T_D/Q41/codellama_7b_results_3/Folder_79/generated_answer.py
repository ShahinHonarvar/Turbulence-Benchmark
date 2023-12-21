
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_set = set()
    # Loop through both lists and check for identical elements between index 4 and index 4
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            identical_set.add(list1[i])
    return identical_set
