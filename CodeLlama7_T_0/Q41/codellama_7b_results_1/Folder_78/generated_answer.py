
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 43 and index 51, both inclusive
    for element in common_elements:
        count = 0
        for i in range(len(list1)):# Check if the element occurs at least once in list1 between index 43 and index 51, both inclusive
            if list1[i] == element and i >= 43 and i <= 51:
                count += 1
        for j in range(len(list2)):# Check if the element occurs at least once in list2 between index 43 and index 51, both inclusive
            if list2[j] == element and j >= 43 and j <= 51:
                count += 1
        # If the element occurs at least once in both lists between index 43 and index 51, both inclusive, add it to the result set
        if count > 0:
            result.add(element)
    return result
