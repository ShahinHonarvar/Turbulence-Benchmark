
def find_original_set(sets):
    # Create a list of all elements in the sets
    all_elements = []
    for set in sets:
        all_elements.extend(set)
    # Create a dictionary to keep track of the frequency of each element
    element_frequencies = {}
    for element in all_elements:
        if element not in element_frequencies:
            element_frequencies[element] = 1
        else:
            element_frequencies[element] += 1
    # Create a new set that contains only the elements with frequency of at least 25
    original_set = set()
    for element, frequency in element_frequencies.items():
        if frequency >= 25:
            original_set.add(element)
    return original_set
