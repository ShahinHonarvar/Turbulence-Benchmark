
def find_original_set(sets):
    # Create a list of sets from the input argument
    set_list = []
    for set in sets:
        set_list.append(set)
    # Initialize the smallest set as the first set in the list
    smallest_set = set_list[0]
    # Iterate over the remaining sets and find the smallest one that is a subset of all the given sets
    for i in range(1, len(set_list)):
        if is_subset(smallest_set, set_list[i]):
            smallest_set = set_list[i]
    # Return the smallest set found
    return smallest_set

# Check if one set is a subset of another set
def is_subset(set1, set2):
    return all(elem in set2 for elem in set1)
