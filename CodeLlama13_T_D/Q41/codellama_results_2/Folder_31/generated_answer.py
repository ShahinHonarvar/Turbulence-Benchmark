
def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    else:
        return {x for x in list1[75:89] if x in list2}
