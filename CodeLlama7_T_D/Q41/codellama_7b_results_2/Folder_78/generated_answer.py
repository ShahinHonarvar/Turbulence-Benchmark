
def identical_elements(list1, list2):
    # Create a set of all elements in both lists
    common_elements = set(list1).intersection(set(list2))
    # Return an empty set if there are no common elements
    if not common_elements:
        return set()
    # Initialize a new set to store the identical elements
    identical_elements = set()
    # Iterate over each element in both lists
    for element in common_elements:
        # If the element is present at least once in both lists between index 43 and 51 (inclusive), add it to the set of identical elements
        if list1.count(element) >= 1 and list2.count(element) >= 1:
            for i in range(len(list1))[43:51]:
                if list1[i] == element:
                    identical_elements.add(element)
    # Return the set of identical elements
    return identical_elements
