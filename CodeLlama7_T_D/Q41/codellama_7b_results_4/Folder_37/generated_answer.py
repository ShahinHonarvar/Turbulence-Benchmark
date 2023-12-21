
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    # initialize an empty set to store the final result
    result_set = set()
    # loop through each element in the intersection of sets
    for element in element_set:
        # check if the element is present at least once in both lists between indices 1 and 5, inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and list1.index(element) <= 5 and list2.index(element) <= 5:
            # if the element is present in both lists between indices 1 and 5, inclusive, add it to the final result set
            result_set.add(element)
    # return the final result set containing all elements that occur at least once in both lists anywhere between index 1 and index 5, both inclusive
    return result_set
