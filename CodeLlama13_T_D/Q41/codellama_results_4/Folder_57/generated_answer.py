
def identical_elements(list1, list2):
    # initialize a set to store the common elements
    common_elements = set()
    
    # loop through both lists from index 27 to 55, both inclusive
    for i in range(27, 56):
        # check if the element at the current index is present in both lists
        if list1[i] == list2[i]:
            # add the common element to the set
            common_elements.add(list1[i])
    
    # return the set of common elements
    return common_elements
