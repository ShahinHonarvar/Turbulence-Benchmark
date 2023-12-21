
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Loop through the list of integers
    for i in range(2, len(my_list)):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # Add the even integer to the new list
            even_ints.append(my_list[i])
    return even_ints
