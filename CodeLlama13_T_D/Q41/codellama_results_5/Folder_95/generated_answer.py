
def identical_elements(list1, list2):
    indices = [i for i in range(82, 87)]
    return {item for item in set(list1[indices]) & set(list2[indices])}
