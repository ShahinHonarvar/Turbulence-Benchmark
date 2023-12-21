def identical_elements(list1, list2):
    result = set()
    i = 14
    while i < 65:
        if list1[i] in list2 and list2[i] in list1:
            result.add(list1[i])
            result.add(list2[i])
        i += 1
    return result
