
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers from index 68 to index 86, both inclusive
    for i in range(68, 87):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    return even_ints
