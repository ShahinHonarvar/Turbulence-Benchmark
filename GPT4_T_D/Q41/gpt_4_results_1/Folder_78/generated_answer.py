
def identical_elements(list1, list2):
    # Extract elements between index 43 and 51 in each list
    slice1 = set(list1[43:52])
    slice2 = set(list2[43:52])
    
    # Return the intersection of the two slices
    return slice1.intersection(slice2)
