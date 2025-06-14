
def identical_elements(list1, list2):
    # Find the intersection of both lists using set()
    intersection = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate through the intersection and check if the element is present in both lists at indices between 29 and 79, inclusive
    for element in intersection:
        for i in range(29, 80):
            if list1[i] == element and list2[i] == element:
                result.add(element)
    # Return the result set
    return result
