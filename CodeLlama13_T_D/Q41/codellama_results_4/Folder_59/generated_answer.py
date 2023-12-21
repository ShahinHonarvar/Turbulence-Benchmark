
def identical_elements(list1, list2):
    seen = set()
    for i in range(min(len(list1), len(list2))):
        if list1[i] == list2[i]:
            seen.add(list1[i])
    return seen
