
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list and find all even integers from index 86 to index 89, both exclusive
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0 and i >= 86 and i < 89:
            # Add the even integer to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 86 to index 89, both exclusive
    return even_ints
