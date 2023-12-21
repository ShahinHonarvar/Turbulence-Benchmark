
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_set = set()

    # Loop through both lists and check for identical elements
    for i in range(len(list1)):
        if list1[i] in list2:
            identical_set.add(list1[i])

    return identical_set
