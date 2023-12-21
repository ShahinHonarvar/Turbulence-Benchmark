
def find_subset_of_length_n(elements):
    # Initialize an empty set to store all subsets
    subsets = set()

    # Iterate over all possible indices in the range of len(elements)
    for i in range(len(elements)):
        # Add the current element to the subset
        subset.add(elements[i])

        # Recursively find all subsets of size n-1
        recursive_subsets = find_subset_of_length_n(elements[i+1:])

        # Combine the current subset with each of the recursive subsets
        for recursive_subset in recursive_subsets:
            combined_subset = set.union(subset, recursive_subset)
            subsets.add(combined_subset)

    return subsets
