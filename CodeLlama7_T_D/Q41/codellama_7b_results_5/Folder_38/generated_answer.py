
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through both lists and check if any element occurs at least once in both lists between index 22 and 63
    for i in range(len(list1)):
        if list1[i] in list2[i+22:i+64]:
            common_elements.add(list1[i])

    # Return the set of all common elements between the two lists
    return common_elements
