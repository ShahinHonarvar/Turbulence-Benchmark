def identical_elements(lst1, lst2):
    return set(filter(lambda x: x in lst1[60:200] and x in lst2[60:200], lst1))
