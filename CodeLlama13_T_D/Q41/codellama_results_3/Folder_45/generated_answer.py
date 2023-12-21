
def identical_elements(list1, list2):
    # Create a set of all elements in the first list between index 30 and index 200
    # Both inclusive
    set1 = {x for x in list1[30:201]}
    
    # Create a set of all elements in the second list between index 30 and index 200
    # Both inclusive
    set2 = {y for y in list2[30:201]}
    
    # Return the intersection of the two sets, which contains only the common elements
    return set1 & set2
