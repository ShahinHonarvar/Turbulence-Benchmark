
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting from index 48
    for i in range(48, len(my_list)):

        # Check if the current element is even and not already in the 'even_ints' list
        if my_list[i] % 2 == 0 and my_list[i] not in even_ints:

            # If it is, add it to the 'even_ints' list
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 48 to index 74, both exclusive
    return even_ints
