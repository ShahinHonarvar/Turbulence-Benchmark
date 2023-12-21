
def all_odd_ints_exclusive(my_list):
    # Create a slice of the list from index 86 to index 90, both exclusive
    slice = my_list[86:90]
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the slice and append each odd integer to the list
    for i in slice:
        if i % 2 != 0:
            odd_ints.append(i)
    # Return the list of all odd integers from index 86 to index 90, both exclusive
    return odd_ints
