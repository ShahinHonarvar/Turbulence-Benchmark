
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list of integers, starting at index 50 and ending at index 92 (both exclusive)
    for i in range(50, 92):

        # If the current integer is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 50 to index 92 (both exclusive)
    return even_ints
