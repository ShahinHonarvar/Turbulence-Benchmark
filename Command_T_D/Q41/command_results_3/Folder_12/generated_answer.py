def identical_elements(list1, list2):
    result = set()
    for i in range(14, 65):
        if (i in list1 and i in list2) or (i in list1 and list2[i-14] in list2) or (i in list2 and list1[i-14] in list1):
            result.add(i)
    return result
