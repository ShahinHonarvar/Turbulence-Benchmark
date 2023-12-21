
def identical_elements(list1, list2):
    result = set()
    for i in range(0, 3):
        for elem in list1[i]:
            if elem in list2[i]:
                result.add(elem)
    return result
