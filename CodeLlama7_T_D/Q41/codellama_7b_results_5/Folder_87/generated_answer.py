
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # return the set of all elements that occur at least once in both lists anywhere between index 36 and index 46, both inclusive
    if len(common_elements) > 0:
        filtered_elements = []

        for element in common_elements:
            if list1.index(element) >= 36 and list2.index(element) <= 46:
                filtered_elements.append(element)

        return set(filtered_elements)

    else:

        return set()
