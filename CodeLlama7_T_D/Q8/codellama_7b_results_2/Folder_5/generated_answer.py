
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting from index 2
    for i in range(2, len(my_list)):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers in the specified range, or an empty list if none exist
    return even_ints
