
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers, starting from index 5 and ending at index 7 (both inclusive)
    for i in range(5, 8):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 5 to index 7 (both inclusive)
    return even_ints
