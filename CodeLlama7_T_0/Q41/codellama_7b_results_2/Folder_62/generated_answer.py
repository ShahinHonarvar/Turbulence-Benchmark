
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the result
    result = set()
    # Iterate over the common elements and check if they occur at least once in both lists between index 91 and index 99, inclusive
    for element in common_elements:
        count = 0
        for i in range(len(list1)):
            if list1[i] == element:
                count += 1
                if count >= 2:
                    result.add(element)
                    break

        for j in range(len(list2)):
            if list2[j] == element:
                count += 1
                if count >= 2:
                    result.add(element)
                    break

    # Return the set of identical elements

    return result
