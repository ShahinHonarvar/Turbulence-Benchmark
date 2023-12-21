
def find_original_set(sets):
    # Find the smallest set in the input list
    smallest_set = min(sets, key=len)
    # Initialize an empty set to store the original set
    original_set = set()

    # Loop through each element in the smallest set
    for element in smallest_set:
        # If the element is not already in the original set, add it
        if element not in original_set:
            original_set.add(element)

    return original_set
