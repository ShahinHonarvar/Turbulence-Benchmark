
def identical_elements(list1, list2):
    return {x for i, x in enumerate(list1) if i >= 62 and i <= 99 and x in list2}
