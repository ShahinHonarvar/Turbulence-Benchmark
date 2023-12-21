
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list from index 10 to index 100, both exclusive
    for i in range(10, 100):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, append it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 10 to index 100, both exclusive
    return even_ints
