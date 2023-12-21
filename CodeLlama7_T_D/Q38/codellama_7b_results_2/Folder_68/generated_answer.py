
def find_subset_of_length_n(my_set):
    # Initialize a list to store all subsets of size 3
    all_subsets = []
    # Iterate through all possible combinations of elements in the set
    for i in range(len(my_set)):
        for j in range(i+1, len(my_set))):
            for k in range(j+1, len(my_set))):
                # Add each subset of size 3 to the list
                all_subsets.append((my_set[i], my_set[j], my_set[k])))
    return len(all_subsets))
