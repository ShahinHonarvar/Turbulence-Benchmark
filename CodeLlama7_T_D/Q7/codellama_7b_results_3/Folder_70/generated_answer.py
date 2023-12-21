
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list and append any even integers to the new list
    for i in range(28, 32 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the new list of even integers
    return even_ints
