
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list, starting from index 41 and ending at index 69 (both exclusive)
    for i in range(41, 70):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range (both exclusive)
    return even_ints
