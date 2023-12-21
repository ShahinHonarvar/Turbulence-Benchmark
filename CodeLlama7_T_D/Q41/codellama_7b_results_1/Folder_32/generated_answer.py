
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the desired elements
    desired_elements = set()
    # Iterate through the common elements and check if they occur at least once in both lists between index 21 and index 97, inclusive
    for element in common_elements:
        count = 0
        for i in range(len(list1)):
            if list1[i] == element:
                count += 1
                if count >= 2 and i >= 21 and i <= 97:
                    desired_elements.add(element)
                    break

    return desired_elements
