
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the results
    matching_elements = set()

    # loop through each element in the common elements set
    for element in common_elements:
        # check if the element occurs at least once in both lists between index 20 and 200, both inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 20 and list1.index(element) <= 200) and (list2.index(element) >= 20 and list2.index(element) <= 200)):
            # if the element occurs at least once in both lists between index 20 and 200, both inclusive, add it to the matching elements set
            matching_elements.add(element)

    return matching_elements
