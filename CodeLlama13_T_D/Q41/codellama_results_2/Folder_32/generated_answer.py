
def identical_elements(list1, list2):
    indices = range(21, 98)
    return set(e for i in indices if e in list1[i] and e in list2[i])
