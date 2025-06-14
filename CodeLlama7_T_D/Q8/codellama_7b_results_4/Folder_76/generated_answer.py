
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 361 to index 643, both exclusive
    for i in range(361, 644):
        # If the current element is even, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 361 to index 643, both exclusive
    return even_ints
