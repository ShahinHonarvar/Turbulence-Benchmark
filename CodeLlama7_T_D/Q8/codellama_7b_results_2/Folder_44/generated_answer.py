
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers starting from index 81
    for i in range(81, len(my_list)):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 81 to index 86, both exclusive
    return even_ints
