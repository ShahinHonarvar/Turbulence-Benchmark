
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers from index 75 to index 94, both inclusive
    for i in range(75, 95):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # Add the even integer to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 75 to index 94, both inclusive
    return even_ints
