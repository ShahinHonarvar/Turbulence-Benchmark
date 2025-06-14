
def all_even_ints_inclusive(my_list):
    # Find the starting index of the range
    start_index = 75

    # Find the ending index of the range
    end_index = 88

    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and append the even integers to the 'even_ints' list
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 75 to index 88, both inclusive
    return even_ints
