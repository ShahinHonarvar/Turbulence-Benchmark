
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate over the common elements and check if they appear at least once in both lists between index 25 and index 87, inclusive
    for element in common_elements:
        count1 = list1.count(element)
        count2 = list2.count(element)
        if count1 >= 25 and count2 >= 25 and count1 <= 87 and count2 <= 87:
            result.add(element)
    # Return the set of identical elements found in both lists
    return result
