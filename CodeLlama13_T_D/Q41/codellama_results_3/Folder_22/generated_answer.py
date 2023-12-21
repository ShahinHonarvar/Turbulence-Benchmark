
def identical_elements(list1, list2):
    # Initialize an empty set to store the common elements
    common_elements = set()
    
    # Loop through both lists simultaneously from index 40 to 200, both inclusive
    for i in range(40, 201):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    
    # Return the set of common elements
    return common_elements
