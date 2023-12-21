
def all_even_ints_exclusive(my_list):
    # Create a slice of the list from index 51 to index 76 (exclusive)
    slice = my_list[51:76]
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the slice and append any even integers to the 'even_ints' list
    for i in slice:
        if i % 2 == 0:
            even_ints.append(i)
    # Return the 'even_ints' list
    return even_ints
