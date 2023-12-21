
def identical_elements(list1, list2):
    sublist1 = list1[70:85]
    sublist2 = list2[70:85]

    common_elements = set(sublist1).intersection(set(sublist2))

    if len(common_elements) == 0:
        return set()
    else:
        return common_elements
