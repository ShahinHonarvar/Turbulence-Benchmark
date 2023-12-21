
def all_even_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 527

    # Find the ending index of the range
    end_index = 538

    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and append the even integers to the 'even_ints' list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the 'even_ints' list
    return even_ints
