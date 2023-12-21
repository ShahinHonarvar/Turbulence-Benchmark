
def identical_elements(list1, list2):
    set1 = set(list1[31:35])
    set2 = set(list2[31:35])
    intersection = set1 & set2
    
    return intersection
