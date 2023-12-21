
def identical_elements(list1, list2):
    set1 = set(list1[20:201])
    set2 = set(list2[20:201])
    result = set1.intersection(set2)
    return result 
