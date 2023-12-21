
def all_odd_ints_exclusive(my_list):
    # Create a slice of the list starting at index 36 and ending at index 85 (exclusive)
    slice = my_list[36:85]
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the slice and append any odd integers to the odd_ints list
    for i in slice:
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints
