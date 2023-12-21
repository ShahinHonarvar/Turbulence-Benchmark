
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list of integers, starting from index 43 and ending at index 51 (both inclusive)
    for i in range(43, 52):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 43 to index 51 (both inclusive), or an empty list if no even integers exist in the specified range
    return even_ints
