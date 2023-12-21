
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the results
    result = set()
    # iterate over each element in the intersection of sets
    for element in common_elements:
        # check if the element occurs at least once in both lists between indices 1 and 8, inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and list1.index(element) <= 8 and list2.index(element) <= 8:
            # add the element to the result set
            result.add(element)
    # return the result set
    return result
