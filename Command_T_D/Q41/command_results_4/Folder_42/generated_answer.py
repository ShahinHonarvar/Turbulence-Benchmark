def identical_elements(lst1, lst2):
    if len(lst1) != len(lst2):
        return set()
    else:
        return set(lst1[29:79] + lst2[29:79])
