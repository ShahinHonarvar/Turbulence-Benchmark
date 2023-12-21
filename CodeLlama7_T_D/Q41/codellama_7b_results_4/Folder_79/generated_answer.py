
def identical_elements(list1, list2):
    # Create a set to store the identical elements
    identical_set = set()
    # Loop through both lists and check if any element occurs at least once in both lists
    for i in range(4, len(list1)):
        for j in range(4, len(list2)):
            if list1[i] == list2[j]:
                identical_set.add(list1[i])
    # Return the set of identical elements
    return identical_set
