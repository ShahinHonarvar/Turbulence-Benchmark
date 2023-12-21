
def identical_elements(list1, list2):
    seen = set()
    for i in range(22, 89):
        if list1[i] == list2[i]:
            seen.add(list1[i])
    return seen
