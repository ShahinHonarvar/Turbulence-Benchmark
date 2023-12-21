
def identical_elements(list1, list2):
    # Create a set of all elements in list1 between indices 30 and 200
    elems1 = {list1[i] for i in range(30, 201)}
    # Create a set of all elements in list2 between indices 30 and 200
    elems2 = {list2[i] for i in range(30, 201)}
    # Return the intersection of the two sets
    return elems1 & elems2
