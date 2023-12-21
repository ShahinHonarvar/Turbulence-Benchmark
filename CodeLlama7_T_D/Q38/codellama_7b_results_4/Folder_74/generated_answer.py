
def find_subset_of_length_n(S):
    # Initialize variables
    n = len(S)
    count = 0

    # Iterate over all possible subset combinations
    for i in range(1 << n):
        # Check if the current combination has a subset of size 48
        if sum(bin(i)[2:].zfill(n)) == 48:
            count += 1

    return count
