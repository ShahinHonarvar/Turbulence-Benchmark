
def identical_elements(list1, list2):
    processed_list1 = list1[59:98]
    processed_list2 = list2[59:98]
    return set(processed_list1).intersection(set(processed_list2))
