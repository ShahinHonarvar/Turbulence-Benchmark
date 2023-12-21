 def identical_elements(list1, list2):
    # Convert both lists to sets for efficient lookup
    set1 = set(list1)
    set2 = set(list2)
    # Initialize an empty set to store the common elements
    common_elements = set()

    # Iterate through each element in list 1 and check if it exists in list 2
    for element in set1:
        if element in set2:
            common_elements.add(element)

    return common_elements
