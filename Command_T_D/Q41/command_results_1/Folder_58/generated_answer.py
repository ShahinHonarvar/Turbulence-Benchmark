def identical_elements(lst1, lst2):
    i = 209
    j = 556
    identical = set()
    while i < j:
        if lst1[i] in lst2[i]:
            identical.add(lst1[i])
        if lst2[i] in lst1[i]:
            identical.add(lst2[i])
        i += 1
    return identical
