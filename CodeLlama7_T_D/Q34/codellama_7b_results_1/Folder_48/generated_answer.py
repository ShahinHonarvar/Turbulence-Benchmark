
def find_original_set(sets):
    # Create a list of all the elements in the given sets
    all_elements = []
    for s in sets:
        all_elements += list(s)

    # Create a dictionary to keep track of the frequency of each element

    element_freq = {}

    for e in all_elements:
        if e not in element_freq:
            element_freq[e] = 1

        else:
            element_freq[e] += 1

    # Find the smallest set that contains all the given sets

    min_set = None

    for s in sets:

        if len(s) == 0:

            continue


        min_set = s

        break


    for e in element_freq:

        if element_freq[e] > len(min_set):

            min_set.add(e)

    return min_set
