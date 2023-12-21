
def identical_elements(list1, list2):
    range_list = list1[23:24] + list2[23:24]
    return set([x for x in range_list if range_list.count(x) > 1])
