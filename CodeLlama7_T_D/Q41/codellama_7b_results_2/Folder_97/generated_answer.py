
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate through each element in the set and check if it occurs at least once in both lists between index 40 and index 80, inclusive
    for element in elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        # Check if the element occurs at least once in both lists between index 40 and index 80, inclusive
        if count1 >= 1 and count2 >= 1:
            for i in range(40, 81):
                if list1[i] == element or list2[i] == element:
                    result.add(element)
    # Return the set of all elements that occur at least once in both lists between index 40 and index 80, inclusive
    return result
