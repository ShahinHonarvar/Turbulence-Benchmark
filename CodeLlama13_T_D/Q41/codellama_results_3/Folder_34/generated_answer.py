
def identical_elements(list1, list2):
    # Create a set to store the common elements between both lists
    common_elements = set()

    # Iterate over both lists simultaneously and compare their corresponding elements at indexes 60 to 200 (both inclusive)
    for i in range(60, 201):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])

    # Return the set of common elements between both lists
    return common_elements
