
def find_subset_of_length_n(elements):
    # Calculate the number of subsets of size 21
    return (2 ** len(elements)) - (len(elements) + 1)
