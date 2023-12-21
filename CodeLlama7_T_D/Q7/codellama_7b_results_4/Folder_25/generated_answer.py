
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(29, 94):
        # If the current element is even, add it to the output list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the output list of all even integers from the specified range, or an empty list if no even integers exist in the specified range
    return even_ints
