
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the results
    matching_elements = set()

    # Iterate over the common elements and check if they occur at least once in both lists between index 43 and index 51, inclusive
    for element in common_elements:
        count = 0

        # Check if the element occurs at least once in list1 between indices 43 and 51, inclusive
        for i in range(43, len(list1)):
            if list1[i] == element:
                count += 1

                # If the element occurs at least once in both lists between index 43 and 51, inclusive, add it to the matching elements set
                if count >= 2:
                    matching_elements.add(element)

                    # Break out of the inner loop since we have found a match
                    break

        # If the element does not occur at least once in both lists between index 43 and 51, inclusive, continue checking for other matches
        if count < 2:
            continue


    # Return the set of matching elements

    return matching_elements
