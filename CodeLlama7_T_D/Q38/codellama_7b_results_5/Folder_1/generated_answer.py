
def find_subset_of_length_n(my_set, n):
    # Initialize a counter variable to keep track of the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(1 << len(my_set)):
        # Check if the current combination has exactly 'n' elements
        if sum(bin(i)[2:].zfill(len(my_set))) == n:
            # Increment the counter by 1 since we have found a subset of size 'n'
            count += 1

    # Return the number of subsets of size 'n'
    return count
