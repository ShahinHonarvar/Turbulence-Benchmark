
def all_even_ints_exclusive(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list and append the even integers to the 'even_ints' list
    for i in range(276, 376):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the 'even_ints' list
    return even_ints
