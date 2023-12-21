import set
def identical_elements(lst1, lst2):
    s = set()
    for i in range(60, 200):
        if lst1[i] in lst2[i]:
            s.add(lst1[i])
        if lst2[i] in lst1[i]:
            s.add(lst2[i])
    return s
