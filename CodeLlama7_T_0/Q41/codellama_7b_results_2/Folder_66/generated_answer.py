
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 50 and index 54, both inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        if count1 >= 1 and count2 >= 1:
            # If the element occurs at least once in both lists between index 50 and index 54, both inclusive, add it to the result set
            for i in range(50, 55):
                if list1[i] == element or list2[i] == element:
                    result.add(element)
    # Return the result set
    return result
