
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers and append the even integers to the empty list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 0 to index 6, both exclusive
    return even_ints
