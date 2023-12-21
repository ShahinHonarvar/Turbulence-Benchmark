
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of the input list
    for i in range(4, len(my_list)):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, append it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 4 to index 4, both inclusive
    return even_ints
