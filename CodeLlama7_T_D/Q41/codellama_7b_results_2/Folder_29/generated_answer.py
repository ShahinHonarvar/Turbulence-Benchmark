 def identical_elements(list1, list2):
    # Check if the lists are of the same size and have at least one element between index 59 and 97 (inclusive)
    if len(list1) != len(list2) or not any(59 <= i < 98 for i in range(len(list1)))):
        # If there are no such elements, return an empty set
        return set()



    # Create a set of all elements in list1 between index 59 and 97 (inclusive)
    elements_in_list1 = {list1[i] for i in range(59, 98)}


    # Return the intersection of this set with the set of all elements in list2 that are also in elements_in_list1
    return elements_in_list1 & set(list2)
