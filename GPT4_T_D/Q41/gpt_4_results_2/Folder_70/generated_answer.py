
def identical_elements(list1, list2):
    first_sub_list = list1[28:33]
    second_sub_list = list2[28:33]
    return set([element for element in first_sub_list if element in second_sub_list])
