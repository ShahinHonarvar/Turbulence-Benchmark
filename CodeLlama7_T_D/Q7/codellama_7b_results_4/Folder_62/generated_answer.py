
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(91, 100):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the output list
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 91 to index 99, both inclusive
    return even_ints
