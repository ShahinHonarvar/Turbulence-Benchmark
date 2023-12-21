
def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the result
    result = set()
    # iterate over each element in the common set
    for element in common_elements:
        # check if the element occurs at least once in both lists between index 31 and index 72, both inclusive
        if list1.count(element) >= 1 and list2.count(element) >= 1 and (list1.index(element) >= 31 and list1.index(element) <= 72) and (list2.index(element) >= 31 and list2.index(element) <= 72)):
            # if the element occurs at least once in both lists between index 31 and index 72, both inclusive, add it to the result set
            result.add(element)
    # return the result set
    return result
