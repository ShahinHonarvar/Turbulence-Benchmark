
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers
    for i in range(18, 60):
        # Check if the current element is even and not already in the 'even_ints' list
        if my_list[i] % 2 == 0 and my_list[i] not in even_ints:
            # Add the current element to the 'even_ints' list
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 18 to index 60, both exclusive
    return even_ints
