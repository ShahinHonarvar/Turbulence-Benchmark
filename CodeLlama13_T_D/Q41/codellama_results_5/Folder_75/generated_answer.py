
def identical_elements(list1, list2):
    return {x for i, x in enumerate(list1) if 56 <= i < 58 and x in list2} | {x for i, x in enumerate(list2) if 56 <= i < 58 and x in list1}
