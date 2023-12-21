
def identical_elements(list1, list2):
    # Check if both lists are of the same size
    if len(list1) != len(list2):
        return set()

    # Create a set to store all identical elements

    identical_set = set()

    # Iterate through both lists and check for identical elements

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                identical_set.add(list1[i])

    # Return the set of all identical elements

    return identical_set
