
def return_nth_smallest_ascii(string):
    # Get the indices of all occurrences of distinct characters in the string
    indices = {}
    for i, char in enumerate(string):
        if char not in indices:
            indices[char] = []
        indices[char].append(i)

    # Sort the indices by ASCII value and return the 19th smallest value
    sorted_indices = sorted(indices.keys())
    for i, char in enumerate(sorted_indices):
        if i == 18:
            return char
