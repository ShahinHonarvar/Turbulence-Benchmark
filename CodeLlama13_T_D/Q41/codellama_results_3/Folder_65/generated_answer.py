
def identical_elements(list1, list2):
    # Get the elements between indices 56 and 98 of both lists
    sublist1 = list1[56:99]
    sublist2 = list2[56:99]
    
    # Create a set of all elements that occur in both lists
    common_elements = set(sublist1).intersection(set(sublist2))
    
    return common_elements
