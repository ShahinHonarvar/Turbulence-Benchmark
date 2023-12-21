
def identical_elements(list1, list2):
    return {item for item in list1[:6] if item in list2[:6]}
