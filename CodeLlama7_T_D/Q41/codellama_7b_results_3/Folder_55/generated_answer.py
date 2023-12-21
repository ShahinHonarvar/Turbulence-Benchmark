
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_elements = set()

    # Iterate over both lists and check for identical elements
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                identical_elements.add(list1[i])

    # Return the set of identical elements
    return identical_elements
