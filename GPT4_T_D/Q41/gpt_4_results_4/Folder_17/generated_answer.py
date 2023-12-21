
def identical_elements(list1, list2):
    list1_subsection = list1[62:79]
    list2_subsection = list2[62:79]

    common_elements = set(list1_subsection) & set(list2_subsection)

    return common_elements
