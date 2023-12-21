
def identical_elements(list1, list2):
    set1 = set(list1[17:79]) # elements from index 17 to 78 in list1
    set2 = set(list2[17:79]) # elements from index 17 to 78 in list2
    
    return set1.intersection(set2) # set of elements that occur in both sets
