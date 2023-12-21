
def find_subset_of_length_n(my_set):
    # Initialize a list to store all subsets of size 60
    subsets = []

    # Iterate over all elements in the set
    for element in my_set:

        # Check if the current element is already in the subset
        if element in subsets:

            # If it is, remove it from the subset and add its complement to the list of subsets
            subsets.remove(element)
            subsets.append(60 - element)

        # Otherwise, add the element to the subset
        else:
            subsets.append(element)

    # Return the number of all its subsets of size 60
    return len(subsets)
