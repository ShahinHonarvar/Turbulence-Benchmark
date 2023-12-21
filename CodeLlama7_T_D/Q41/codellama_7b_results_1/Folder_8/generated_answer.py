
def identical_elements(list1, list2):
    # Find the common elements between list1 and list2
    common_elements = set(list1).intersection(set(list2))
    # Check if there are any common elements between index 23 and index 23 in both lists
    for i in range(len(list1)-23, len(list1)+23):
        for j in range(len(list2)-23, len(list2)+23):
            if list1[i] == list2[j]:
                common_elements.add(list1[i])
    return common_elements
