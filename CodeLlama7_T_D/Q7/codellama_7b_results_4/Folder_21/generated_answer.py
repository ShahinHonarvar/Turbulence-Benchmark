
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list and append each even integer to the new list
    for i in range(639, 975 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 639 to index 975, both inclusive
    return even_ints
