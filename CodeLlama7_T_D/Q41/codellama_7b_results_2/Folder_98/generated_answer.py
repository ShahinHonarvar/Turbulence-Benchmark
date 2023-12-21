 def identical_elements(list1, list2):
    # create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # initialize an empty set to store the results
    results = set()
    # iterate over each element in the intersection of sets
    for element in common_elements:
        # check if the element is present at least once in both lists
        # starting from index 0 and ending at index 5, inclusive
        if list1.count(element) > 0 and list2.count(element) > 0:
            # if the element is present in both lists, add it to the results set
            results.add(element)
    # return the results set
    return results
