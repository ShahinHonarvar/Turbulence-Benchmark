
def all_even_ints_exclusive(my_list):
    # Create a slice of the list from index 56 to index 88, both exclusive
    slice_of_list = my_list[56:88]
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the slice and append any even integers to the 'even_ints' list
    for i in slice_of_list:
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints
