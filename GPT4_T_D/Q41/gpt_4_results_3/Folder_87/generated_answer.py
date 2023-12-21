
def identical_elements(list1, list2):
    # Set comprehension to check for common elements between index 36 and 46
    common_elements = {x for x in list1[36:47] if x in list2[36:47]}
    return common_elements
