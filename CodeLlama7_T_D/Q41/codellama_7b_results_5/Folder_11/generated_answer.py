
def identical_elements(list1, list2):
    # Initialize an empty set to store the elements that are present in both lists
    common_elements = set()

    # Iterate over the elements of the first list

    for element in list1:

        # Check if the current element is also present in the second list

        if element in list2:

            # If the element is present, add it to the set of common elements

            common_elements.add(element)

    return common_elements
