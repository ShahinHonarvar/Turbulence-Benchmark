
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the final result
    final_result = set()
    # Iterate through each element in the common elements set
    for element in common_elements:
        # Check if the element is present in both lists at indices between 91 and 99, inclusive
        if list1.index(element) >= 91 and list1.index(element) <= 99 and list2.index(element) >= 91 and list2.index(element) <= 99:
            # If the element is present in both lists at the desired indices, add it to the final result set
            final_result.add(element)
    # Return the final result set
    return final_result
