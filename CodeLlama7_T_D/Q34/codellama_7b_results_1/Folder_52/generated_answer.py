
def find_original_set(sets):
    # Create a list of sets from the input
    set_list = [set() for _ in range(len(sets))]
    # Add each set to the appropriate index in the list
    for i, s in enumerate(sets):
        set_list[i] |= s
    # Return the smallest set from the list
    return min(set_list)
