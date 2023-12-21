
def find_original_set(sets):
    # Create a list of all elements in the sets
    elements = []
    for set in sets:
        elements += list(set)

    # Create a dictionary to keep track of elements and their counts

    element_counts = {}

    for element in elements:

        if element not in element_counts:
            element_counts[element] = 1

        else:
            element_counts[element] += 1

    # Find the smallest set that contains all elements

    smallest_set = None

    for element, count in element_counts.items():

        if count == len(sets):

            if smallest_set is None:

                smallest_set = {element}


            else:

                smallest_set.add(element)


    return smallest_set
