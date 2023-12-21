
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list from index 18 to index 37, both exclusive
    for i in range(18, 37):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 18 to index 37, both exclusive
    return even_ints
