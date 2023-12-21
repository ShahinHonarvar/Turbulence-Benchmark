
def identical_elements(list1, list2):
    indices = set(range(32, 36))
    return set(list1) & set(list2) & indices if set(list1) & set(list2) & indices else set()
