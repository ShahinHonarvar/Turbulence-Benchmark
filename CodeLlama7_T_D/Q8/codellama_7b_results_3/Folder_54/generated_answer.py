
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list from index 27 to index 34, both exclusive
    for i in range(26, len(my_list)):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 27 to index 34, both exclusive
    return even_ints
