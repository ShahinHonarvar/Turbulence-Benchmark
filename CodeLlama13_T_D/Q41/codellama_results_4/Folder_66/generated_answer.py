
def identical_elements(list1, list2):
    set_list = set()
    for i in range(50, 55):
        if list1[i] == list2[i]:
            set_list.add(list1[i])
    return set_list
