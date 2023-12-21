
def identical_elements(list1, list2):
    set1 = set(list1[70:85])
    set2 = set(list2[70:85])

    identical_values = set1.intersection(set2)

    return identical_values
