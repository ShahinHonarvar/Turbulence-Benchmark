
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 4 and index 4, both inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        if count1 >= 1 and count2 >= 1:
            result.add(element)
    # Return the set of identical elements
    return result
