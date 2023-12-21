
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if there are no common elements
    if not common_elements:
        return set()
    else:
        # Initialize a set to store the elements that meet the condition
        filtered_elements = set()

        # Loop through each element in both lists and check if it meets the condition
        for element in common_elements:
            # If the element is found at least once in both lists between index 75 and 94, inclusive, add it to the filtered set
            if list1.index(element) >= 75 and list2.index(element) <= 94:
                filtered_elements.add(element)
        # Return the filtered set of elements that meet the condition
        return filtered_elements
