
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 43 and index 86, both inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        # If the element occurs at least once in both lists between index 43 and index 86, both inclusive, add it to the result set
        if count1 > 0 and count2 > 0:
            for i in range(43, 87):
                if list1[i] == element or list2[i] == element:
                    result.add(element)
    # Return the result set
    return result
