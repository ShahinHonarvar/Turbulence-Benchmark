
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result_set = set()
    # Loop through each element in the set and check if it occurs at least once in both lists
    for element in element_set:
        list1_count = list1.count(element)
        list2_count = list2.count(element)
        # If the element occurs at least once in both lists, add it to the result set
        if list1_count > 0 and list2_count > 0:
            result_set.add(element)
    # Return the result set
    return result_set
