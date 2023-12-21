
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting at index 28 and ending at index 40
    for i in range(28, 41):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 28 to index 40, both inclusive
    return even_ints
