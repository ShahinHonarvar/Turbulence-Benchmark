
def identical_elements(list1, list2):
    list1 = list1[40:81]
    list2 = list2[40:81]

    return set(list1).intersection(set(list2))
