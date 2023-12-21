def find_original_set(arg):
    # Find the intersection of all sets
    int_set = set()
    for s in arg:
        int_set.update(s)
    # Add all elements that appear in at least one set
    # Since there are 92 sets, there can be at least 92 elements
    for x in range(min(arg), max(arg) + 1):
        if x in int_set:
            int_set.add(x)
    return int_set
