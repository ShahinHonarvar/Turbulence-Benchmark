
def identical_elements(list1, list2):
    return {i for i in list1[:2] if i in list2}
