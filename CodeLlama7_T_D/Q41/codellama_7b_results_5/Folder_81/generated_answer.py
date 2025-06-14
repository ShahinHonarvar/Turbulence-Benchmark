
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    # initialize an empty set to store the identical elements
    identical_elements = set()

    # iterate over the set of all elements and check if it appears at least once in both lists between index 10 and index 100, inclusive
    for element in element_set:
        count = 0

        # check if the element is present in list1 between index 10 and index 100, inclusive
        if element in list1[10:100+1]:
            count += 1

        # check if the element is present in list2 between index 10 and index 100, inclusive
        if element in list2[10:100+1]:
            count += 1

        # if the element appears at least once in both lists between index 10 and index 100, inclusive, add it to the set of identical elements
        if count >= 2:
            identical_elements.add(element)

    return identical_elements
