
def find_original_set(sets):
    # Create a set to store all the elements
    all_elements = set()

    for s in sets:
        all_elements |= s

    # Create a new set with the smallest possible size
    original_set = set()

    # Iterate through all the elements and add them to the original set
    for element in all_elements:
        if all(element in s for s in sets):
            original_set.add(element)

    return original_set
