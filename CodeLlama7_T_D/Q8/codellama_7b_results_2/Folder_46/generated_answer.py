
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the list of integers, starting from index 20 (inclusive) and ending at index 43 (exclusive)
    for i in range(20, len(my_list)):
        # Check if the current integer is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range
    return even_ints
