
def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return "The lists must be of the same size."
          
    set1 = set(list1[30:201])
    set2 = set(list2[30:201])

    identical_set = set1.intersection(set2)

    return identical_set
