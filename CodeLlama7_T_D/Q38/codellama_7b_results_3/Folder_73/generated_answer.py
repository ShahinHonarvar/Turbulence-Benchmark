
def find_subset_of_length_n(set):
    # Initialize a counter variable to keep track of the number of subsets
    count = 0

    # Iterate over all possible subsets of size n
    for subset in itertools.combinations(set, n):
        if len(subset) == n:
            count += 1

    return count
