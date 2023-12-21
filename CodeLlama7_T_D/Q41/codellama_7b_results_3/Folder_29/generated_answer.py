
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate over both lists and check if any element occurs in both lists
    for i in range(59, 97+1):
        if list1[i] in list2:
            common_elements.add(list1[i])

    return common_elements
