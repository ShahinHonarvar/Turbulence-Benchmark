
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers, starting at index 87 and ending at index 95 (both exclusive)
    for i in range(87, 95):
        # If the current element is an even integer, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers in the specified range
    return even_ints
