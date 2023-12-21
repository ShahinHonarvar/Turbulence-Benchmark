
def identical_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    index_range = set(range(56, 67))
    result = set()
    
    for element in index_range:
        if element in set1 and element in set2:
            result.add(element)
    
    return result
