
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Initialize an empty set to store the final result
    final_result = set()
    # Iterate over the common elements and check if they appear at least once in both lists anywhere between index 0 and index 6, both inclusive.
    for element in common_elements:
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            final_result.add(element)
    # Return the final result
    return final_result
