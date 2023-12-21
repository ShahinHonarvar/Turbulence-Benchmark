
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list, starting at index 32 and ending at index 35 (both inclusive)
    for i in range(32, 36):
        # If the current element is even, add it to the list of even integers
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 32 to index 35 (both inclusive)
    return even_ints
