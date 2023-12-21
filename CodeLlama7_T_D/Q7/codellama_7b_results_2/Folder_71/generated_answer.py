
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of the input list
    for i in range(26, 53):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 26 to index 52, both inclusive
    return even_ints
