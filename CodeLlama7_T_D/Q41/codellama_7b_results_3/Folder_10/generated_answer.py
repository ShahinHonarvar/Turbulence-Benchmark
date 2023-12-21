
def identical_elements(list1, list2):
    # Initialize a set to store the identical elements
    identical_set = set()

    # Iterate over both lists and check for identical elements between index 25 and index 59
    for i in range(25, len(list1)):
        for j in range(25, len(list2)):
            if list1[i] == list2[j]:
                # If an identical element is found, add it to the set
                identical_set.add(list1[i])

    return identical_set
