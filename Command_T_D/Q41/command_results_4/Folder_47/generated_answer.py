def identical_elements(list1, list2):
    res = set()
    for i in range(37, 77):
        if list1[i] in list2 and list2[i] in list1:
            res.add(list1[i])
            res.add(list2[i])
    return res
