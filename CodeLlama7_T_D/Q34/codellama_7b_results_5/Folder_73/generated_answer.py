
def find_original_set(sets):
    # Create a list of all the elements in the sets
    all_elements = []
    for s in sets:
        all_elements += list(s)

    # Create a dictionary to keep track of the frequency of each element

    element_freq = {}
    for e in all_elements:
        if e not in element_freq:
            element_freq[e] = 0
        element_freq[e] += 1

    # Find the smallest set that contains all the elements with frequency of at least 19

    smallest_set = None
    for s in sets:
        subset = True
        for e in s:
            if element_freq[e] < 19:
                subset = False
                break

        if subset:
            if smallest_set is None or len(smallest_set) > len(s):
                smallest_set = s

    return smallest_set
