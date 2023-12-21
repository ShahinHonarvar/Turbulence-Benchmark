
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list of integers, starting at index 68
    for i in range(68, len(my_list)):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers in the specified range
    return even_ints
