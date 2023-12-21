
def all_odd_ints_exclusive(my_list):
    # Define a range of indices to iterate over
    indices = range(59, 94)
    # Create an empty list to store the odd integers
    odd_ints = []
    # Iterate over the indices and append each odd integer to the list
    for i in indices:
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
