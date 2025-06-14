
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the list of integers, starting from index 29 and ending at index 51 (both inclusive)
    for i in range(29, 52):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers found in the specified range, or an empty list if none were found
    return even_ints
