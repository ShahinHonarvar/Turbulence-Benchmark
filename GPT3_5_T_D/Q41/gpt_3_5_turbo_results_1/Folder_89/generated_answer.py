
def identical_elements(list1, list2):
    start = max(56, len(list1) - 1)
    end = min(82, len(list1))
    return set(list1[start:end+1]) & set(list2[start:end+1])
