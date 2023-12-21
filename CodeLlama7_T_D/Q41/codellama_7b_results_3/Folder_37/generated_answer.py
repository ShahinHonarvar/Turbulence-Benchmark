
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    element_set = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result_set = set()
    # Iterate through each element in the set and check if it occurs at least once in both lists anywhere between index 1 and index 5, both inclusive
    for element in element_set:
        count = 0
        for i in range(1, 6):
            if element in list1[i:] and element in list2[:-i]:
                count += 1
        # If the element occurs at least once in both lists anywhere between index 1 and index 5, both inclusive, add it to the result set
        if count > 0:
            result_set.add(element)
    return result_set
