
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and append the even integers to the 'even_ints' list
    for i in range(25, 80):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 25 to index 80, both exclusive
    return even_ints
