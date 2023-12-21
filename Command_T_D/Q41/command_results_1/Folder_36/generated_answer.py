import set
def identical_elements(list1, list2):
    res = set()
    for i in range(246, 750):
        if list1[i] in list2[i]:
            res.add(list1[i])
    return res
