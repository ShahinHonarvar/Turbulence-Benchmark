
def all_even_ints_exclusive(my_list):
    # Check if the input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")

    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and check if each element is even
    for i in range(2, 8):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 2 to index 8, both exclusive
    return even_ints
