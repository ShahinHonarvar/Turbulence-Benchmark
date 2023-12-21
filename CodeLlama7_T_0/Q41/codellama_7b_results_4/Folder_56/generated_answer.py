
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 1 and index 8, both inclusive
    for element in common_elements:
        count = 0
        for i in range(len(list1)):
            if list1[i] == element:
                count += 1
                if count >= 2:
                    result.add(element)
                    break

    # Return the set of identical elements

    return result
