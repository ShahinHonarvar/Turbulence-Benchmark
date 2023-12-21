
def identical_elements(list1, list2):
    if len(list1) < 201 or len(list2) < 201:
        return set()
        
    return set(list1[200:201]).intersection(set(list2[200:201]))
