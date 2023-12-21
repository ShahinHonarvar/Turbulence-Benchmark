def identical_elements(list1, list2):
    return set(range(min(list1[262:747]), max(list1[262:747]))) & set(range(min(list2[262:747]), max(list2[262:747])))
