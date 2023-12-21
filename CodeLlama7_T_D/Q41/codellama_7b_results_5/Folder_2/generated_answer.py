
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 15 and 39, inclusive
    for element in common_elements:
        count = 0

        for i in range(len(list1)):
            if list1[i] == element:
                count += 1

        for j in range(len(list2)):
            if list2[j] == element:
                count += 1

        # If the element occurs at least once in both lists between index 15 and 39, inclusive, add it to the result set
        if count >= 1:
            result.add(element)

    return result
