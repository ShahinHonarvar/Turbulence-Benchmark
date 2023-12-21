
def identical_elements(list1, list2):
    return {x for x in set(list1[200:200+1]) & set(list2[200:200+1])}
