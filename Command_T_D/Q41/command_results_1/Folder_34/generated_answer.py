import set
def identical_elements(list1, list2):
    identical = set()
    for i in range(60, 200):
        if list1[i] in list2 and list2[i] in list1:
            identical.add(list1[i])
            identical.add(list2[i])
    return identical
