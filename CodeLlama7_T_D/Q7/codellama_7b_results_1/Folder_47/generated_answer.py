
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list of integers, starting from index 37 and ending at index 76 (both inclusive)
    for i in range(37, 77):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 37 to index 76 (both inclusive)
    return even_ints
